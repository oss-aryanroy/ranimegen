import random
import aiohttp
from bs4 import BeautifulSoup

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



def parse_html(image):
    anime_list = []
    soup = BeautifulSoup(image, 'lxml')
    for link in soup.find_all('a'):
            anime_list.append(link.get('href'))
    actual_list_reduced = anime_list[83:300]
    anime_name_list = [ anime for anime in actual_list_reduced if "authorize" not in anime and "login" not in anime and "genre" not in anime and "producer" not in anime and "episode" not in anime and "video" not in anime]
    some_anime_link = random.choice(anime_name_list)
    correct_anime_name = some_anime_link.split('/')[-1].split('_')
    anime_name_final = ""
    for elements in correct_anime_name:
        anime_name_final += f"{elements} "
    return anime_name_final
