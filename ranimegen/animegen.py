import asyncio
import aiohttp
import random
from bs4 import BeautifulSoup
from ranimegen.workers import get_anime, get_info, parse_html

class RandomAnime:
    def __init__(self):
        pass


    async def suggestanime():
        categories = ['1/Action','2/Adventure','4/Comedy','6/Demons','9/Ecchi', '8/Drama','10/Fantasy','11/Game','36/Slice_of_Life','16/Magic','10/Fantasy','27/Shounen','7/Mystery']
        image = await get_anime(categories)
        loop = asyncio.get_event_loop()
        anime_name_final = await loop.run_in_executor(None, parse_html, image)
        main_res = await get_info(anime_name_final)
        return main_res
