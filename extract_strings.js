const fs = require('fs');

function extractStrings(content) {
    let en_strings = {};
    let ko_strings = {};
    const matches = [...content.matchAll(/JSON\.parse\('({.*?})'\)/g)];
    for (let i = 0; i < matches.length; i++) {
        try {
            const str = eval("'" + matches[i][1] + "'");
            const obj = JSON.parse(str);
            if (obj.COMMON_OPEN_DISCORD === 'Open Discord') {
                Object.assign(en_strings, obj);
            } else if (obj.COMMON_OPEN_DISCORD === 'Discord 열기') {
                Object.assign(ko_strings, obj);
            }
        } catch(e) {}
    }
    return { en: en_strings, ko: ko_strings };
}

const content = fs.readFileSync(process.argv[2], 'utf-8');
const result = extractStrings(content);
console.log(JSON.stringify(result));
