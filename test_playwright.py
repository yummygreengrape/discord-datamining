from playwright.sync_api import sync_playwright

def extract_strings_with_playwright(locale="ko-KR"):
    strings = {}
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context(locale=locale)
            page = context.new_page()
            page.goto('https://canary.discord.com/login', timeout=60000)
            page.wait_for_selector('div') # wait for app to load
            
            script = """
            () => {
                let req;
                window.webpackChunkdiscord_app.push([
                    [Symbol()], {}, (r) => { req = r; }
                ]);
                let extracted = {};
                for (const key in req.c) {
                    const module = req.c[key].exports;
                    if (module && typeof module === 'object') {
                        if (module.default && module.default.COMMON_OPEN_DISCORD) {
                            extracted = module.default;
                            break;
                        }
                        if (module.COMMON_OPEN_DISCORD) {
                            extracted = module;
                            break;
                        }
                    }
                }
                return extracted;
            }
            """
            strings = page.evaluate(script)
            browser.close()
    except Exception as e:
        print(f"Failed to extract {locale} strings:", e)
    return strings

print(len(extract_strings_with_playwright("ko-KR")))
