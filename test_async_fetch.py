import requests, re, json, asyncio, aiohttp

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            if response.status == 200:
                return await response.text()
    except:
        pass
    return ""

async def main():
    html = requests.get('https://canary.discord.com/app').text
    js_urls = ['https://canary.discord.com' + s for s in re.findall(r'src="(/assets/[^"]+)"', html)]
    chunk_map = None
    for url in js_urls:
        content = requests.get(url).text
        matches = re.findall(r'\{(?:\d+:"[a-f0-9]+",?)+\}', content)
        for m in matches:
            if len(m) > 1000:
                chunk_map = json.loads(m.replace(':', '":').replace(',', ',"').replace('{', '{"'))
                break
        if chunk_map:
            break

    if not chunk_map:
        print("Chunk map not found")
        return

    urls = [f"https://canary.discord.com/assets/{k}.{v}.js" for k, v in chunk_map.items()]
    print(f"Fetching {len(urls)} chunks...")

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, u) for u in urls]
        contents = await asyncio.gather(*tasks)

    print(f"Downloaded {len(contents)} chunks.")
    
    ko_strings = {}
    en_strings = {}

    for content in contents:
        # Find JSON.parse('...')
        for match in re.finditer(r'JSON\.parse\(([\'\"])(.*?)\1\)', content):
            jstr = match.group(2)
            jstr = jstr.replace('\\"', '"').replace('\\\\', '\\').replace("\\'", "'")
            try:
                data = json.loads(jstr)
                if 'COMMON_OPEN_DISCORD' in data:
                    if data['COMMON_OPEN_DISCORD'] == 'Discord 열기':
                        ko_strings.update(data)
                    elif data['COMMON_OPEN_DISCORD'] == 'Open Discord':
                        en_strings.update(data)
            except:
                pass

    print("English strings:", len(en_strings))
    print("Korean strings:", len(ko_strings))

asyncio.run(main())
