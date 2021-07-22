import random
import asyncio
import aiohttp
from bs4 import BeautifulSoup


async def get_anime(categories) -> str and bool:
    sock = random.choice(categories)
    async with aiohttp.ClientSession() as session:
               async with session.get("https://myanimelist.net/anime/genre/" + sock, timeout=10) as response:
                    image = await response.text()
    if sock.split('/')[1].lower() == "hentai":
        answer = False
    else:
        answer = True
    return image, answer


async def get_info_nsfw(query) -> dict:
    await asyncio.sleep(1.12)
    async with aiohttp.ClientSession() as cs:        
                 async with cs.get(f'https://api.jikan.moe/v3/search/anime?q={query}&limit=10') as r:
                     result = await r.json()
    return result
                 

async def get_info(name) -> dict:
    async with aiohttp.ClientSession() as cs:
                 async with cs.get(f'https://kitsu.io/api/edge/anime?filter[text]={name}') as r:
                        result = await r.json()
                 return result


def parse_html(image):   
    soup = BeautifulSoup(image, 'lxml')
    anime_list = [link.get('href') for link in soup.find_all('a')] 
    actual_list_reduced = anime_list
    anime_name_list = [ anime for anime in actual_list_reduced if anime and "https://myanimelist.net/anime/" in anime]
    some_anime_link = random.choice(anime_name_list)
    correct_anime_name = " ".join(some_anime_link.split('/')[-1].split('_'))
    return correct_anime_name



