from playwright.sync_api import sync_playwright

def test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('https://canary.discord.com/login')
        page.wait_for_timeout(3000) # wait 3 seconds
        
        script = """
        () => {
            let req;
            window.webpackChunkdiscord_app.push([
                [Symbol()], {}, (r) => { req = r; }
            ]);
            let all_keys = new Set();
            for (const key in req.c) {
                const module = req.c[key].exports;
                if (module && typeof module === 'object') {
                    let target = module.default || module;
                    if (typeof target === 'object') {
                        Object.keys(target).forEach(k => all_keys.add(k));
                    }
                }
            }
            return Array.from(all_keys).filter(k => typeof k === 'string' && k.includes('OPEN_DISCORD'));
        }
        """
        keys = page.evaluate(script)
        print("Keys containing OPEN_DISCORD:", keys)
        browser.close()

test()
