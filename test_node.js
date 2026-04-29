const https = require('https');
https.get('https://canary.discord.com/assets/84804.2e015603f5d8ff86.js', (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        const matches = [...data.matchAll(/JSON\.parse\('({.*?})'\)/g)];
        for (let i = 0; i < matches.length; i++) {
            try {
                // To safely parse JS string literals into JS string, we can use eval
                const str = eval("'" + matches[i][1] + "'");
                const obj = JSON.parse(str);
                if (obj.COMMON_OPEN_DISCORD) {
                    if (obj.COMMON_OPEN_DISCORD === 'Discord 열기') {
                        console.log('Korean is at index', i);
                    } else if (obj.COMMON_OPEN_DISCORD === 'Open Discord') {
                        console.log('English is at index', i);
                    }
                }
            } catch(e) {}
        }
    });
});
