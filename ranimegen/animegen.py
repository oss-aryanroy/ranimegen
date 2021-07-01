import aiohttp
import random
from bs4 import BeautifulSoup
from ranimegen.workers import get_anime, get_info

class RandomAnime:
    def __init__(self):
        pass


    async def suggestanime(self):
        categories = ['1/Action','2/Adventure','4/Comedy','6/Demons','9/Ecchi', '8/Drama','10/Fantasy','11/Game','36/Slice_of_Life','16/Magic','10/Fantasy','27/Shounen','7/Mystery']
        image = await get_anime(categories)
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
        main_res = await get_info(anime_name_final)
        return main_res
