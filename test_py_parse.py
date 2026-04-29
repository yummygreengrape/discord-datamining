import requests, re, json

content = requests.get('https://canary.discord.com/assets/84804.2e015603f5d8ff86.js').text
en_strings = {}
ko_strings = {}
for match in re.finditer(r'JSON\.parse\(([\'\"])(.*?)\1\)', content):
    jstr = match.group(2)
    jstr = jstr.replace('\\"', '"').replace('\\\\', '\\').replace("\\'", "'")
    try:
        data = json.loads(jstr)
        if 'COMMON_OPEN_DISCORD' in data:
            if data['COMMON_OPEN_DISCORD'] == 'Open Discord':
                en_strings.update(data)
            elif data['COMMON_OPEN_DISCORD'] == 'Discord 열기':
                ko_strings.update(data)
    except Exception as e:
        pass

print("English:", len(en_strings), "Korean:", len(ko_strings))
