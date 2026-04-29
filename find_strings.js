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
    
    let ko_chunks = [];
    for (let url of js_urls) {
        let content = await get(url);
        const matches = [...content.matchAll(/JSON\.parse\('({.*?})'\)/g)];
        for (let i = 0; i < matches.length; i++) {
            try {
                const str = eval("'" + matches[i][1] + "'");
                const obj = JSON.parse(str);
                
                // test if it's Korean by checking a known key
                if (obj['COMMON_OPEN_DISCORD'] === 'Discord 열기') {
                    ko_chunks.push(Object.keys(obj).length);
                }
            } catch(e) {}
        }
    }
    console.log("Korean chunks found:", ko_chunks);
})();
