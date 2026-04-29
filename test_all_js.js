const fs = require('fs');
const https = require('https');

function get(url) {
    return new Promise(resolve => {
        https.get(url, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
            res.on('error', () => resolve(''));
        }).on('error', () => resolve(''));
    });
}

(async () => {
    let html = await get('https://canary.discord.com/app');
    let js_urls = [...html.matchAll(/src="(\/assets\/[^"]+)"/g)].map(m => 'https://canary.discord.com' + m[1]);
    
    let en_strings = {};
    let ko_strings = {};
    
    for (let url of js_urls) {
        let content = await get(url);
        const matches = [...content.matchAll(/JSON\.parse\('({.*?})'\)/g)];
        for (let i = 0; i < matches.length; i++) {
            try {
                const str = eval("'" + matches[i][1] + "'");
                const obj = JSON.parse(str);
                
                // Identify language by some known keys if possible
                // It's hard to know which object is which language if we just look at one key
                // because some chunks might not have COMMON_OPEN_DISCORD.
                // Let's just assume the 30th is English and 40th is Korean for all chunks? No.
            } catch(e) {}
        }
    }
})();
