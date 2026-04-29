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
    
    let chunk_map = null;
    for (let url of js_urls) {
        let content = await get(url);
        const matches = [...content.matchAll(/\{(?:\d+:"[a-f0-9]+",?)+\}/g)];
        for (let m of matches) {
            if (m[0].length > 1000) {
                // To safely parse JS map, we add quotes
                let json_str = m[0].replace(/([0-9]+):/g, '"$1":');
                chunk_map = JSON.parse(json_str);
                break;
            }
        }
        if (chunk_map) break;
    }

    if (!chunk_map) {
        console.log("No chunk map");
        return;
    }

    let urls = Object.entries(chunk_map).map(([k,v]) => `https://canary.discord.com/assets/${k}.${v}.js`);
    console.log("Fetching", urls.length, "chunks...");
    
    // fetch concurrently in batches
    let contents = [];
    for(let i=0; i<urls.length; i+=50) {
        let batch = urls.slice(i, i+50);
        let res = await Promise.all(batch.map(u => get(u)));
        contents.push(...res);
    }

    let en_strings = {};
    let ko_strings = {};
    
    for (let content of contents) {
        const matches = [...content.matchAll(/JSON\.parse\('({.*?})'\)/g)];
        for (let i = 0; i < matches.length; i++) {
            try {
                const str = eval("'" + matches[i][1] + "'");
                const obj = JSON.parse(str);
                
                if (obj['COMMON_OPEN_DISCORD'] === 'Discord 열기') {
                    Object.assign(ko_strings, obj);
                } else if (obj['COMMON_OPEN_DISCORD'] === 'Open Discord') {
                    Object.assign(en_strings, obj);
                }
            } catch(e) {}
        }
    }
    console.log("English:", Object.keys(en_strings).length);
    console.log("Korean:", Object.keys(ko_strings).length);
})();
