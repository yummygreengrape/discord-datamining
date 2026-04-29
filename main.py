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
    
    experiments = set()
    api_endpoints = set()

    exp_pattern = re.compile(r'id:"([0-9]{4}-[0-9]{2}_[^"\s]+)"')
    api_pattern = re.compile(r'"(/api/v[0-9]+/[^"]*?)"')

    for js_url in js_files:
        if "sentry" in js_url or "wasm" in js_url:
            continue
        try:
            content = requests.get(js_url, timeout=10).text
        except:
            continue
            
        # Extract experiments
        for match in exp_pattern.findall(content):
            experiments.add(match)
            
        # Extract APIs
        for match in api_pattern.findall(content):
            api_endpoints.add(match)
            
    return {
        "build_hash": build_hash,
        "experiments": sorted(list(experiments)),
        "api_endpoints": sorted(list(api_endpoints)),
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

    prev_exps = set(previous_state.get("experiments", []))
    curr_exps = set(current_data["experiments"])
    new_exps = sorted(list(curr_exps - prev_exps))
    
    prev_apis = set(previous_state.get("api_endpoints", []))
    curr_apis = set(current_data["api_endpoints"])
    new_apis = sorted(list(curr_apis - prev_apis))
    
    changes = {
        "build_hash": current_data["build_hash"],
        "new_experiments": new_exps,
        "new_api_endpoints": new_apis,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }
    
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
