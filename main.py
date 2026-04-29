import time
import requests
import re
import json
import os
import subprocess
from datetime import datetime, timezone

def get_html(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

def download_chunk(url, dest_path):
    try:
        r = requests.get(url, timeout=10)
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write(r.text)
        return r.text
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return ""

def fetch_canary_data():
    html = get_html("https://canary.discord.com/login")
    if not html: return None

    build_hash = None
    hash_match = re.search(r'buildId":"([^"]+)"', html)
    if hash_match:
        build_hash = hash_match.group(1)
    else:
        print("Could not find build hash")
        return None
    
    js_urls = []
    for match in re.finditer(r'src="(/assets/[^"]+\.js)"', html):
        js_urls.append("https://canary.discord.com" + match.group(1))
    
    chunk_map = None
    for url in js_urls:
        content = get_html(url)
        matches = re.finditer(r'\{(?:\d+:"[a-f0-9]+",?)+\}', content)
        for m in matches:
            text = m.group(0)
            if len(text) > 1000:
                json_str = re.sub(r'([0-9]+):', r'"\1":', text)
                try:
                    chunk_map = json.loads(json_str)
                    break
                except:
                    pass
        if chunk_map:
            break
            
    if chunk_map:
        for k, v in chunk_map.items():
            js_urls.append(f"https://canary.discord.com/assets/{k}.{v}.js")
            
    return {
        "build_hash": build_hash,
        "js_urls": list(set(js_urls)) # deduplicate
    }

def run_git_command(cmd, cwd):
    try:
        subprocess.run(cmd, cwd=cwd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Git command failed: {cmd}\n{e.stderr.decode()}")

def main():
    data_dir = "data"
    canary_dir = "canary"
    os.makedirs(data_dir, exist_ok=True)
    os.makedirs(canary_dir, exist_ok=True)
    
    state_file = os.path.join(data_dir, "previous_state.json")
    changes_file = os.path.join(data_dir, "latest_changes.json")
    history_file = os.path.join(data_dir, "history.json")
    
    print("Discord Datamining Docker Daemon Started.")

    while True:
        try:
            previous_state = {}
            if os.path.exists(state_file):
                with open(state_file, 'r', encoding='utf-8') as f:
                    try:
                        previous_state = json.load(f)
                    except:
                        pass

            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Checking for updates...")
            current_data = fetch_canary_data()
            if not current_data:
                time.sleep(300)
                continue

            build_hash = current_data["build_hash"]
            prev_hash = previous_state.get("build_hash")

            if build_hash == prev_hash:
                print(f"No update detected. Current build: {build_hash}")
                if os.environ.get("GITHUB_ACTIONS"):
                    print("Running in GitHub Actions, exiting after one run.")
                    break
                time.sleep(600) # Check every 10 minutes
                continue

            print(f"Update detected! {prev_hash} -> {build_hash}")
            
            # Clean up old canary directory
            subprocess.run(f"rm -rf {canary_dir}/*", shell=True)

            experiments = {}
            api_endpoints = {}

            endpoint_pattern = re.compile(r'([A-Z_]+[A-Z0-9_]*)\s*:\s*(?:(?:[a-zA-Z_$][a-zA-Z_$0-9]*)=>|(?:\([^)]*\))\s*=>)?\s*`([^`]+)`')
            string_endpoint_pattern = re.compile(r'([A-Z_]+[A-Z0-9_]*)\s*:\s*"(/api/[^"]+)"')

            js_urls = current_data["js_urls"]
            print(f"Downloading {len(js_urls)} JS chunks...")
            
            for i, url in enumerate(js_urls):
                filename = url.split('/')[-1]
                dest_path = os.path.join(canary_dir, filename)
                content = download_chunk(url, dest_path)
                
                # Extract APIs
                for name, url_template in endpoint_pattern.findall(content):
                    if name in ['type']: continue
                    url_str = re.sub(r'\$\{[^}]+\}', ':param', url_template)
                    api_endpoints[name] = url_str

                for name, url_str in string_endpoint_pattern.findall(content):
                    if name not in api_endpoints:
                        api_endpoints[name] = url_str

                # Extract experiments
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

            print("Running js-beautify...")
            try:
                subprocess.run(f"find {canary_dir} -name '*.js' | xargs -n 50 js-beautify -r -q", shell=True, check=True)
            except Exception as e:
                print("js-beautify failed, skipping.", e)

            # --- Update History Logic ---
            prev_exps_raw = previous_state.get("experiments", {})
            prev_exps_dict = prev_exps_raw if isinstance(prev_exps_raw, dict) else {k: {"id": k, "kind": "unknown", "treatments": []} for k in prev_exps_raw}
            curr_exps_dict = experiments
            
            new_exps_keys = sorted(list(set(curr_exps_dict.keys()) - set(prev_exps_dict.keys())))
            del_exps_keys = sorted(list(set(prev_exps_dict.keys()) - set(curr_exps_dict.keys())))
            new_exps = [curr_exps_dict[k] for k in new_exps_keys]
            del_exps = [prev_exps_dict[k] for k in del_exps_keys]

            prev_apis_raw = previous_state.get("api_endpoints", {})
            prev_apis_dict = prev_apis_raw if isinstance(prev_apis_raw, dict) else {k: "unknown" for k in prev_apis_raw}
            curr_apis_dict = api_endpoints

            new_apis_keys = sorted(list(set(curr_apis_dict.keys()) - set(prev_apis_dict.keys())))
            del_apis_keys = sorted(list(set(prev_apis_dict.keys()) - set(curr_apis_dict.keys())))
            new_apis = [{"name": k, "url": curr_apis_dict[k]} for k in new_apis_keys]
            del_apis = [{"name": k, "url": prev_apis_dict[k]} for k in del_apis_keys]

            now_iso = datetime.now(timezone.utc).isoformat()
            
            changes = {
                "build_hash": build_hash,
                "new_experiments": new_exps,
                "deleted_experiments": del_exps,
                "new_api_endpoints": new_apis,
                "deleted_api_endpoints": del_apis,
                "string_changes": {"ko": {"added": {}, "modified": {}, "deleted": {}}, "en": {"added": {}, "modified": {}, "deleted": {}}},
                "timestamp": now_iso
            }

            history_data = {"build_hash": build_hash, "experiments": [], "api_endpoints": [], "strings": []}
            if os.path.exists(history_file):
                with open(history_file, 'r', encoding='utf-8') as f:
                    try:
                        loaded = json.load(f)
                        history_data["experiments"] = loaded.get("experiments", [])
                        history_data["api_endpoints"] = loaded.get("api_endpoints", [])
                        history_data["strings"] = loaded.get("strings", []) # Preserve existing string history manually
                    except: pass

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

            # Save
            with open(history_file, 'w', encoding='utf-8') as f: json.dump(history_data, f, ensure_ascii=False, indent=4)
            with open(os.path.join(data_dir, "experiments.json"), 'w', encoding='utf-8') as f: json.dump(experiments, f, ensure_ascii=False, indent=4)
            with open(os.path.join(data_dir, "api_endpoints.json"), 'w', encoding='utf-8') as f: json.dump(api_endpoints, f, ensure_ascii=False, indent=4)
            
            previous_state["build_hash"] = build_hash
            previous_state["experiments"] = experiments
            previous_state["api_endpoints"] = api_endpoints
            with open(state_file, 'w', encoding='utf-8') as f: json.dump(previous_state, f, ensure_ascii=False, indent=4)
            with open(changes_file, 'w', encoding='utf-8') as f: json.dump(changes, f, ensure_ascii=False, indent=4)

            # Git commit and push
            print("Committing to Github...")
            cwd = os.getcwd()
            run_git_command("git config --global user.name 'Discord Datamining Bot'", cwd)
            run_git_command("git config --global user.email 'bot@discord-archive.com'", cwd)
            run_git_command("git add data/ .gitignore", cwd)
            run_git_command(f'git commit -m "Update Canary Data: {build_hash} [skip ci]"', cwd)
            run_git_command("git push", cwd)

            print("Update complete!")
            if os.environ.get("GITHUB_ACTIONS"):
                print("Running in GitHub Actions, exiting after one run.")
                break
            time.sleep(600)
            
        except Exception as e:
            print(f"Error in main loop: {e}")
            if os.environ.get("GITHUB_ACTIONS"):
                break
            time.sleep(300)

if __name__ == "__main__":
    main()
