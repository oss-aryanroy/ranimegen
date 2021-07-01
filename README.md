# ranimegen
Python Package for Random Anime Generation 

```
pip install ranimegen
``` 

# Usage

```py
from ranimegen.animegen import RandomAnime()


generator = RandomAnime()
myinfo = await generator.suggestanime()

print(myinfo)

...
>>> (json response with anime information from Kitsu's API)
```
