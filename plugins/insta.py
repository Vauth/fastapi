import re 
from aiohttp import ClientSession, ClientTimeout

async def Get(link:str):
    "Get direct links of instagram reels/images"
    pattern = re.search(r'(?:instagram.com)\/(p|reel)\/(.*?)(\/|$)', link)
    if pattern: pType, pID = "videos" if pattern.group(1) == "reel" else "images", pattern.group(2)
    else: return {"success": 0, "detail": "Incorrect instagram url"}
    All = {"success": 1, 'list':[], 'grid': f'https://www.ddinstagram.com/grid/{pID}' if pType == 'images' else 'None'}
    for i in range(1, 11):
        async with ClientSession(timeout=ClientTimeout(total=10)) as session:
            async with session.get(f'https://www.ddinstagram.com/{pType}/{pID}/{i}') as r:
                text = (await r.content.read()).decode('utf-8', errors='ignore')
                if ("Not Found" in text): break
                else: All['list'].append(str(r.url).replace('https://envoy.lol/', ''))
    return All if len(All['list']) != 0 else {"success": 0, "detail": "Deleted or private instagram url"}

  
