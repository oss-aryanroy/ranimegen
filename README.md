# ranimegen
Python Package for Random Anime Generation 

```
pip install ranimegen
``` 

# Usage

```py
from ranimegen import animegen


generator = animegen.RandomAnime()
myinfo = await generator.suggestanime()

print(myinfo)

...
>>> (json response with anime information from Kitsu's API)
```
