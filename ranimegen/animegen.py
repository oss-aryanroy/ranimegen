import asyncio
from ranimegen.errors import InvalidGenre
from ranimegen.workers import get_anime, get_info, parse_html, get_info_nsfw

class RandomAnime:
    def __init__(self):
        self._category = ['1/Action','2/Adventure', '3/Cars', '4/Comedy', '5/Dementia', '6/Demons', '7/Mystery', '8/Drama', '9/Ecchi', '10/Fantasy', '11/Game', '13/Historical', '14/Horror', '15/Kids', '16/Magic', '17/Martial_Arts', '18/Mecha', '19/Music', '20/Parody', '21/Samurai', '22/Romance', '23/School', '24/Sci-Fi', '25/Shoujo', '26/Shoujo_Ai', '27/Shounen', '28/Shounen_Ai', '29/Space', '30/Sports', '31/Super_Power', '32/Vampire', '33/Yaoi', '34/Yuri', '35/Harem', '36/Slice_of_Life', '37/Supernatural', '38/Military']

    @property
    def genres(self):
        return [cat.split('/')[-1].lower() for cat in self._category]


    async def suggestanime(self,*, genre=None, safe=True) -> dict:
        loop = asyncio.get_event_loop()
        categories = self._category
        if safe is False:
            categories.append('12/Hentai')
        if genre:
            categories = [gen for gen in categories for logic in genre.split(' ') if logic.lower() == gen.split('/')[1].lower()]
            if len(categories) == 0:
                raise InvalidGenre('No valid genres in \'{}\' were found'.format(genre))
        if len(categories) > 1:
            image = await get_anime(categories)
            anime_name_final = await loop.run_in_executor(None, parse_html, image[0])
        else:
            if categories[0].split('/')[1].lower() == "hentai":
                image = await get_anime(categories)
            else:
                image = await get_anime(categories)
            anime_name_final = await loop.run_in_executor(None, parse_html, image[0])
        if image[1] is False:
            main_res = await get_info_nsfw(anime_name_final)
        else:
            main_res = await get_info(anime_name_final)
        return main_res
