import requests
import re
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def fetch_canary_data():
    url = "https://canary.discord.com/app"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    
    js_urls = [s.get("src") for s in soup.find_all("script") if s.get("src")]
    css_urls = [s.get("href") for s in soup.find_all("link", rel="stylesheet") if s.get("href")]

    js_files = []
    for s in js_urls:
        if not s.startswith('http'):
            s = "https://canary.discord.com" + s
        js_files.append(s)

    # 보통 Discord 빌드 해시는 HTML 안의 buildNumber로 존재함
    build_hash = "unknown"
    build_match = re.search(r'buildId\s*:\s*"([^"]+)"', html) or re.search(r'buildNumber\s*:\s*"([^"]+)"', html)
    if build_match:
        build_hash = build_match.group(1)
    else:
        # 해시를 찾을 수 없으면 첫 번째 css 파일의 해시값 등으로 대체
        if css_urls:
            m = re.search(r'\.([0-9a-f]+)\.css', css_urls[0])
            if m: build_hash = m.group(1)
    
    experiments = {}
    api_endpoints = {}

    endpoint_pattern = re.compile(r'([A-Z_]+[A-Z0-9_]*)\s*:\s*(?:(?:[a-zA-Z_$][a-zA-Z_$0-9]*)=>|(?:\([^)]*\))\s*=>)?\s*`([^`]+)`')
    string_endpoint_pattern = re.compile(r'([A-Z_]+[A-Z0-9_]*)\s*:\s*"(/api/[^"]+)"')

    for js_url in js_files:
        if "sentry" in js_url or "wasm" in js_url:
            continue
        try:
            content = requests.get(js_url, timeout=10).text
        except:
            continue
            
        # Extract endpoints from backticks with param replacements
        for name, url_template in endpoint_pattern.findall(content):
            if name in ['type']: continue
            url_str = re.sub(r'\$\{[^}]+\}', ':param', url_template)
            api_endpoints[name] = url_str

        # Extract endpoints from simple strings
        for name, url_str in string_endpoint_pattern.findall(content):
            if name not in api_endpoints:
                api_endpoints[name] = url_str

        # Extract apex experiments
        for match in re.finditer(r'id:"([0-9]{4}-[0-9]{2}_[^"\s]+)"', content):
            exp_id = match.group(1)
            start = max(0, match.start() - 100)
            end = min(len(content), match.end() + 300)
            chunk = content[start:end]
            
            kind_match = re.search(r'kind:"([^"]+)"', chunk)
            kind = kind_match.group(1) if kind_match else "unknown"
            
            treat_match = re.search(r'treatments:\[(.*?)\]', chunk)
            treatments = []
            if treat_match:
                treatments_raw = treat_match.group(1)
                for t_label in re.findall(r'label:"([^"]+)"', treatments_raw):
                    treatments.append(t_label)
            
            experiments[exp_id] = {
                "id": exp_id,
                "kind": kind,
                "treatments": treatments
            }
            
    return {
        "build_hash": build_hash,
        "experiments": experiments,
        "api_endpoints": api_endpoints,
        "js_files": js_files,
        "css_files": css_urls
    }


def main():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)
    
    state_file = os.path.join(data_dir, "previous_state.json")
    changes_file = os.path.join(data_dir, "latest_changes.json")
    
    previous_state = {}
    if os.path.exists(state_file):
        with open(state_file, 'r', encoding='utf-8') as f:
            try:
                previous_state = json.load(f)
            except:
                pass

    print("Fetching Discord Canary data...")
    current_data = fetch_canary_data()
    if not current_data:
        print("Failed to fetch data")
        return

    prev_exps_raw = previous_state.get("experiments", {})
    if isinstance(prev_exps_raw, list):
        prev_exps = set(prev_exps_raw)
        prev_exps_dict = {k: {"id": k, "kind": "unknown", "treatments": []} for k in prev_exps_raw}
    else:
        prev_exps = set(prev_exps_raw.keys())
        prev_exps_dict = prev_exps_raw

    curr_exps_dict = current_data["experiments"]
    curr_exps = set(curr_exps_dict.keys())
    
    new_exps_keys = sorted(list(curr_exps - prev_exps))
    del_exps_keys = sorted(list(prev_exps - curr_exps))
    
    new_exps = [curr_exps_dict[k] for k in new_exps_keys]
    del_exps = [prev_exps_dict[k] for k in del_exps_keys]
    
    prev_apis_raw = previous_state.get("api_endpoints", {})
    if isinstance(prev_apis_raw, list):
        prev_apis = set(prev_apis_raw)
        prev_apis_dict = {k: "unknown" for k in prev_apis_raw}
    else:
        prev_apis = set(prev_apis_raw.keys())
        prev_apis_dict = prev_apis_raw

    curr_apis_dict = current_data["api_endpoints"]
    curr_apis = set(curr_apis_dict.keys())
    
    new_apis_keys = sorted(list(curr_apis - prev_apis))
    del_apis_keys = sorted(list(prev_apis - curr_apis))
    
    new_apis = [{"name": k, "url": curr_apis_dict[k]} for k in new_apis_keys]
    del_apis = [{"name": k, "url": prev_apis_dict[k]} for k in del_apis_keys]
    
    now_iso = datetime.now(timezone.utc).isoformat()
    
    changes = {
        "build_hash": current_data["build_hash"],
        "new_experiments": new_exps,
        "deleted_experiments": del_exps,
        "new_api_endpoints": new_apis,
        "deleted_api_endpoints": del_apis,
        "timestamp": now_iso
    }
    
    # 누적 기록 관리 (history.json)
    history_file = os.path.join(data_dir, "history.json")
    history_data = {"experiments": [], "api_endpoints": []}
    if os.path.exists(history_file):
        with open(history_file, 'r', encoding='utf-8') as f:
            try:
                history_data = json.load(f)
            except:
                pass

    # 최초 실행 시 모든 항목을 'added'로 기록
    if not previous_state:
        for k, v in curr_exps_dict.items():
            history_data["experiments"].append({"id": k, "kind": v["kind"], "treatments": v["treatments"], "status": "added", "timestamp": now_iso})
        for k, v in curr_apis_dict.items():
            history_data["api_endpoints"].append({"name": k, "url": v, "status": "added", "timestamp": now_iso})
    else:
        for item in new_exps:
            history_data["experiments"].append({"id": item["id"], "kind": item["kind"], "treatments": item["treatments"], "status": "added", "timestamp": now_iso})
        for item in del_exps:
            history_data["experiments"].append({"id": item["id"], "kind": item["kind"], "treatments": item["treatments"], "status": "deleted", "timestamp": now_iso})
            
        for item in new_apis:
            history_data["api_endpoints"].append({"name": item["name"], "url": item["url"], "status": "added", "timestamp": now_iso})
        for item in del_apis:
            history_data["api_endpoints"].append({"name": item["name"], "url": item["url"], "status": "deleted", "timestamp": now_iso})

    with open(history_file, 'w', encoding='utf-8') as f:
        json.dump(history_data, f, ensure_ascii=False, indent=4)
    
    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(current_data, f, ensure_ascii=False, indent=4)
        
    with open(changes_file, 'w', encoding='utf-8') as f:
        json.dump(changes, f, ensure_ascii=False, indent=4)

    # 개별 항목 저장용
    with open(os.path.join(data_dir, "experiments.json"), 'w', encoding='utf-8') as f:
        json.dump(current_data["experiments"], f, ensure_ascii=False, indent=4)
        
    with open(os.path.join(data_dir, "api_endpoints.json"), 'w', encoding='utf-8') as f:
        json.dump(current_data["api_endpoints"], f, ensure_ascii=False, indent=4)
        
    print(f"Build Hash: {current_data['build_hash']}")
    print(f"New Experiments: {len(new_exps)}")
    print(f"New APIs: {len(new_apis)}")

if __name__ == "__main__":
    main()
