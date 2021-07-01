import random
import aiohttp


async def get_anime(categories):
    async with aiohttp.ClientSession() as session:
               async with session.get("https://myanimelist.net/anime/genre/" + random.choice(categories), timeout=10) as response:
                image = await response.text()
    return image


async def get_info(name):
    async with aiohttp.ClientSession() as cs:
                 async with cs.get(f'https://kitsu.io/api/edge/anime?filter[text]={name}') as r:
                        result = await r.json()
    return result