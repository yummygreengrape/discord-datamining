from playwright.sync_api import sync_playwright
import json

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(locale="en-US")
        page = context.new_page()
        page.goto('https://canary.discord.com/login', timeout=60000)
        page.wait_for_selector('div')
        page.wait_for_timeout(5000) # Wait 5s for modules to load
        
        script = """
        () => {
            let req;
            window.webpackChunkdiscord_app.push([
                [Symbol()], {}, (r) => { req = r; }
            ]);
            
            let all_strings = {};
            for (const key in req.c) {
                const module = req.c[key].exports;
                if (module && typeof module === 'object') {
                    // Look for modules that contain many keys and string values
                    let isStringModule = false;
                    let stringCount = 0;
                    for (const k in module) {
                        if (typeof module[k] === 'string') {
                            stringCount++;
                        }
                    }
                    if (stringCount > 100) {
                        return module;
                    }
                    if (module.default) {
                        let defStringCount = 0;
                        for (const k in module.default) {
                            if (typeof module.default[k] === 'string') {
                                defStringCount++;
                            }
                        }
                        if (defStringCount > 100) {
                            return module.default;
                        }
                    }
                }
            }
            return all_strings;
        }
        """
        
        result = page.evaluate(script)
        print("Extracted strings:", len(result))
        if len(result) > 100:
            with open("data/extracted_strings_test.json", "w") as f:
                json.dump(result, f, indent=2)
        browser.close()

if __name__ == "__main__":
    test()
