# ranimegen
![](https://img.shields.io/pypi/v/ranimegen)

Python Package for Random Anime Generation using BeautifulSoup and KitsuAPI

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

# Output Format: JSON

(About 10 outputs per search) `to access go inside the data keyword and index the list of animes`

```py
{
	'data': [{
		'id': '11',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/11'
		},
		'attributes': {
			'createdAt': '2013-02-20T16:00:24.797Z',
			'updatedAt': '2021-07-01T13:55:03.575Z',
			'slug': 'naruto',
			'synopsis': "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.\nNow, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.\n[Written by MAL Rewrite]",
			'description': "Moments prior to Naruto Uzumaki's birth, a huge demon known as the Kyuubi, the Nine-Tailed Fox, attacked Konohagakure, the Hidden Leaf Village, and wreaked havoc. In order to put an end to the Kyuubi's rampage, the leader of the village, the Fourth Hokage, sacrificed his life and sealed the monstrous beast inside the newborn Naruto.\nNow, Naruto is a hyperactive and knuckle-headed ninja still living in Konohagakure. Shunned because of the Kyuubi inside him, Naruto struggles to find his place in the village, while his burning desire to become the Hokage of Konohagakure leads him not only to some great new friends, but also some deadly foes.\n[Written by MAL Rewrite]",
			'coverImageTopOffset': 209,
			'titles': {
				'en': 'Naruto',
				'en_jp': 'Naruto',
				'ja_jp': 'ナ ルト'
			},
			'canonicalTitle': 'Naruto',
			'abbreviatedTitles': ['NARUTO'],
			'averageRating': '79.74',
			'ratingFrequencies': {
				'2': '585',
				'3': '4',
				'4': '483',
				'5': '13',
				'6': '498',
				'7': '22',
				'8': '2268',
				'9': '48',
				'10': '2694',
				'11': '93',
				'12': '5959',
				'13': '259',
				'14': '15277',
				'15': '587',
				'16': '12028',
				'17': '792',
				'18': '7523',
				'19': '389',
				'20': '22340'
			},
			'userCount': 107919,
			'favoritesCount': 3017,
			'startDate': '2002-10-03',
			'endDate': '2007-02-08',
			'nextRelease': None,
			'popularityRank': 42,
			'ratingRank': 644,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'TV',
			'status': 'finished',
			'tba': '',
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/11/tiny.jpg?1597698839',
				'small': 'https://media.kitsu.io/anime/poster_images/11/small.jpg?1597698839',
				'medium': 'https://media.kitsu.io/anime/poster_images/11/medium.jpg?1597698839',
				'large': 'https://media.kitsu.io/anime/poster_images/11/large.jpg?1597698839',
				'original': 'https://media.kitsu.io/anime/poster_images/11/original.jpg?1597698839',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/11/tiny.jpg?1597701519',
				'small': 'https://media.kitsu.io/anime/cover_images/11/small.jpg?1597701519',
				'large': 'https://media.kitsu.io/anime/cover_images/11/large.jpg?1597701519',
				'original': 'https://media.kitsu.io/anime/cover_images/11/original.jpg?1597701519',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 220,
			'episodeLength': 23,
			'totalLength': 5060,
			'youtubeVideoId': 'j2hiC9BmJlQ',
			'showType': 'TV',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/11/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/11/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/11/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/11/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/11/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/11/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/11/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/11/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/11/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/11/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/11/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/11/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/11/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/11/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/11/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/11/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/11/anime-staff'
				}
			}
		}
	}, {
		'id': '7543',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/7543'
		},
		'attributes': {
			'createdAt': '2013-02-20T17:57:39.629Z',
			'updatedAt': '2021-07-01T13:46:18.591Z',
			'slug': 'the-last-naruto-the-movie',
			'synopsis': 'It has been two years since the Fourth Shinobi World War, and the world is once again existing in harmony—that is, until another threat surfaces and once again puts the planet on the very brink of destruction.\nAmidst the impending catastrophe, Hinata Hyuuga’s sister, Hanabi, is suddenly abducted. Naruto Uzumaki, together with a team of skillful ninjas; Sakura, Sai, Shikamaru, and Hinata, set out to rescue Hanabi from the evil clutches of Toneri Ootsutsuki. While they get closer and closer to completing their mission, they are faced with several adversaries, who will not only test the relationship they have with one another, but also puts the fate of the planet in face of uncertainty. As the clock ticks, the team rushes to end the last battle, fighting for peace...and love.',
			'description': 'It has been two years since the Fourth Shinobi World War, and the world is once again existing in harmony—that is, until another threat surfaces and once again puts the planet on the very brink of destruction.\nAmidst the impending catastrophe, Hinata Hyuuga’s sister, Hanabi, is suddenly abducted. Naruto Uzumaki, together with a team of skillful ninjas; Sakura, Sai, Shikamaru, and Hinata, set out to rescue Hanabi from the evil clutches of Toneri Ootsutsuki. While they get closer and closer to completing their mission, they are faced with several adversaries, who will not only test the relationship they have with one another, but also puts the fate of the planet in face of uncertainty. As the clock ticks, the team rushes to end the last battle, fighting for peace...and love.',
			'coverImageTopOffset': 100,
			'titles': {
				'en': 'The Last: Naruto the Movie',
				'en_jp': 'The Last: Naruto the Movie',
				'en_us': 'The Last: Naruto the Movie',
				'ja_jp': 'THE LAST NARUTO THE MOVIE'
			},
			'canonicalTitle': 'The Last: Naruto the Movie',
			'abbreviatedTitles': ['Naruto Movie 10: Naruto the Movie: The Last,Naruto: Shippuuden Movie 7 - The Last', 'Naruto Movie 10: Naruto the Movie: The Last', 'Naruto: Shippuuden Movie 7 - The Last'],
			'averageRating': '80.12',
			'ratingFrequencies': {
				'2': '132',
				'3': '3',
				'4': '111',
				'5': '7',
				'6': '130',
				'7': '12',
				'8': '491',
				'9': '22',
				'10': '551',
				'11': '39',
				'12': '1122',
				'13': '96',
				'14': '3426',
				'15': '182',
				'16': '2697',
				'17': '231',
				'18': '1704',
				'19': '118',
				'20': '5135'
			},
			'userCount': 24925,
			'favoritesCount': 184,
			'startDate': '2014-12-06',
			'endDate': '2014-12-06',
			'nextRelease': None,
			'popularityRank': 427,
			'ratingRank': 577,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/7543/tiny.jpg?1597697683',
				'small': 'https://media.kitsu.io/anime/poster_images/7543/small.jpg?1597697683',
				'medium': 'https://media.kitsu.io/anime/poster_images/7543/medium.jpg?1597697683',
				'large': 'https://media.kitsu.io/anime/poster_images/7543/large.jpg?1597697683',
				'original': 'https://media.kitsu.io/anime/poster_images/7543/original.jpg?1597697683',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/7543/tiny.jpg?1623049676',
				'small': 'https://media.kitsu.io/anime/cover_images/7543/small.jpg?1623049676',
				'large': 'https://media.kitsu.io/anime/cover_images/7543/large.jpg?1623049676',
				'original': 'https://media.kitsu.io/anime/cover_images/7543/original.jpg?1623049676',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 112,
			'totalLength': 112,
			'youtubeVideoId': 'tA3yE4_t6SY',
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/7543/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/7543/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/7543/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/7543/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/7543/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/7543/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/7543/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/7543/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/7543/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/7543/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/7543/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/7543/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/7543/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/7543/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/7543/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7543/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/7543/anime-staff'
				}
			}
		}
	}, {
		'id': '2245',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/2245'
		},
		'attributes': {
			'createdAt': '2013-02-20T16:35:15.856Z',
			'updatedAt': '2021-07-01T13:52:30.684Z',
			'slug': 'naruto-shippuden-movie-1',
			'synopsis': 'Demons that once almost destroyed the world, are revived by someone. To prevent the world from being destroyed, the demon has to be sealed and the only one who can do it is the shrine maiden Shion from the country of demons, who has two powers; one is sealing demons and the other is predicting the deaths of humans. This time Naruto\'s mission is to guard Shion, but she predicts Naruto\'s death. The only way to escape it, is to get away from Shion, which would leave her unguarded, then the demon, whose only goal is to kill Shion will do so, thus meaning the end of the world. Naruto decides to challenge this "prediction of death," but fails to prove Shion\'s prediction wrong and supposedly dies in vain.\n(Source: Wikipedia)',
			'description': 'Demons that once almost destroyed the world, are revived by someone. To prevent the world from being destroyed, the demon has to be sealed and the only one who can do it is the shrine maiden Shion from the country of demons, who has two powers; one is sealing demons and the other is predicting the deaths of humans. This time Naruto\'s mission is to guard Shion, but she predicts Naruto\'s death. The only way to escape it, is to get away from Shion, which would leave her unguarded, then the demon, whose only goal is to kill Shion will do so, thus meaning the end of the world. Naruto decides to challenge this "prediction of death," but fails to prove Shion\'s prediction wrong and supposedly dies in vain.\n(Source: Wikipedia)',
			'coverImageTopOffset': 100,
			'titles': {
				'en': 'Naruto: Shippuden the Movie',
				'en_jp': 'Naruto: Shippuuden Movie 1',
				'en_us': 'Naruto: Shippuden the Movie',
				'ja_jp': '劇場版NARUTO -ナルト- 疾風伝'
			},
			'canonicalTitle': 'Naruto: Shippuuden Movie 1',
			'abbreviatedTitles': ['Naruto Shippuuden Movie', 'Naruto Movie 4', 'Gekijouban Naruto Shippuuden'],
			'averageRating': '72.86',
			'ratingFrequencies': {
				'2': '66',
				'3': '1',
				'4': '85',
				'5': '2',
				'6': '135',
				'7': '4',
				'8': '436',
				'9': '6',
				'10': '665',
				'11': '21',
				'12': '1394',
				'13': '42',
				'14': '2644',
				'15': '59',
				'16': '1667',
				'17': '38',
				'18': '591',
				'19': '14',
				'20': '1617'
			},
			'userCount': 16397,
			'favoritesCount': 54,
			'startDate': '2007-08-04',
			'endDate': '2007-08-04',
			'nextRelease': None,
			'popularityRank': 705,
			'ratingRank': 2710,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/2245/tiny.jpg?1597697957',
				'small': 'https://media.kitsu.io/anime/poster_images/2245/small.jpg?1597697957',
				'medium': 'https://media.kitsu.io/anime/poster_images/2245/medium.jpg?1597697957',
				'large': 'https://media.kitsu.io/anime/poster_images/2245/large.jpg?1597697957',
				'original': 'https://media.kitsu.io/anime/poster_images/2245/original.jpg?1597697957',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/2245/tiny.jpg?1597703370',
				'small': 'https://media.kitsu.io/anime/cover_images/2245/small.jpg?1597703370',
				'large': 'https://media.kitsu.io/anime/cover_images/2245/large.jpg?1597703370',
				'original': 'https://media.kitsu.io/anime/cover_images/2245/original.jpg?1597703370',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 94,
			'totalLength': 94,
			'youtubeVideoId': None,
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/2245/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/2245/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/2245/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/2245/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/2245/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/2245/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/2245/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/2245/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/2245/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/2245/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/2245/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/2245/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/2245/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/2245/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/2245/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/2245/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/2245/anime-staff'
				}
			}
		}
	}, {
		'id': '1555',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/1555'
		},
		'attributes': {
			'createdAt': '2013-02-20T16:24:49.365Z',
			'updatedAt': '2021-07-01T15:15:43.946Z',
			'slug': 'naruto-shippuden',
			'synopsis': 'It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the mysterious organization of elite rogue ninja, is closing in on their grand plan which may threaten the safety of the entire shinobi world.\n\nAlthough Naruto is older and sinister events loom on the horizon, he has changed little in personality—still rambunctious and childish—though he is now far more confident and possesses an even greater determination to protect his friends and home. Come whatever may, Naruto will carry on with the fight for what is important to him, even at the expense of his own body, in the continuation of the saga about the boy who wishes to become Hokage.\n\n(Source: MAL Rewrite)',
			'description': 'It has been two and a half years since Naruto Uzumaki left Konohagakure, the Hidden Leaf Village, for intense training following events which fueled his desire to be stronger. Now Akatsuki, the mysterious organization of elite rogue ninja, is closing in on their grand plan which may threaten the safety of the entire shinobi world.\n\nAlthough Naruto is older and sinister events loom on the horizon, he has changed little in personality—still rambunctious and childish—though he is now far more confident and possesses an even greater determination to protect his friends and home. Come whatever may, Naruto will carry on with the fight for what is important to him, even at the expense of his own body, in the continuation of the saga about the boy who wishes to become Hokage.\n\n(Source: MAL Rewrite)',
			'coverImageTopOffset': 100,
			'titles': {
				'en': 'Naruto: Shippuden',
				'en_jp': 'Naruto: Shippuuden',
				'en_us': 'Naruto: Shippuden',
				'ja_jp': 'ナルト- 疾風伝'
			},
			'canonicalTitle': 'Naruto: Shippuuden',
			'abbreviatedTitles': ['Naruto Hurricane Chronicles'],
			'averageRating': '83.23',
			'ratingFrequencies': {
				'2': '1018',
				'3': '19',
				'4': '421',
				'5': '14',
				'6': '519',
				'7': '36',
				'8': '2255',
				'9': '49',
				'10': '1856',
				'11': '82',
				'12': '4116',
				'13': '269',
				'14': '10557',
				'15': '574',
				'16': '8225',
				'17': '799',
				'18': '6549',
				'19': '603',
				'20': '31391'
			},
			'userCount': 96476,
			'favoritesCount': 3938,
			'startDate': '2007-02-15',
			'endDate': '2017-03-23',
			'nextRelease': None,
			'popularityRank': 53,
			'ratingRank': 23,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'TV',
			'status': 'finished',
			'tba': '',
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/1555/tiny.jpg?1597696875',
				'small': 'https://media.kitsu.io/anime/poster_images/1555/small.jpg?1597696875',
				'medium': 'https://media.kitsu.io/anime/poster_images/1555/medium.jpg?1597696875',
				'large': 'https://media.kitsu.io/anime/poster_images/1555/large.jpg?1597696875',
				'original': 'https://media.kitsu.io/anime/poster_images/1555/original.jpg?1597696875',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/1555/tiny.jpg?1597702491',
				'small': 'https://media.kitsu.io/anime/cover_images/1555/small.jpg?1597702491',
				'large': 'https://media.kitsu.io/anime/cover_images/1555/large.jpg?1597702491',
				'original': 'https://media.kitsu.io/anime/cover_images/1555/original.jpg?1597702491',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 500,
			'episodeLength': 23,
			'totalLength': 11500,
			'youtubeVideoId': '1dy2zPPrKD0',
			'showType': 'TV',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/1555/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/1555/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/1555/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/1555/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/1555/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/1555/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/1555/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/1555/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/1555/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/1555/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/1555/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/1555/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/1555/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/1555/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/1555/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/1555/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/1555/anime-staff'
				}
			}
		}
	}, {
		'id': '7008',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/7008'
		},
		'attributes': {
			'createdAt': '2013-02-20T17:48:52.898Z',
			'updatedAt': '2021-07-01T13:52:40.945Z',
			'slug': 'naruto-shippuden-movie-6-road-to-ninja',
			'synopsis': "Ten years ago, a gigantic demon beast known as the Nine-Tailed Demon Fox was released from its jinchuuriki by an unknown shinobi wearing a mask. The village of Konohagakure was close to destruction by the attack of the Nine-Tails, but the village was saved by its leader. Minato Namikaze and his wife Kushina Uzumaki—who was the jinchuuriki at the time of the attack—sealed away the demon inside their new born son: Naruto Uzumaki. However, this act of saving the village cost them their lives and they left the future of the ninja world to Naruto.\nWith the demon fox sealed away, things continued as normal. However, the peace of the village would not last long, for Pain, Konan, Itachi Uchiha, Kisame Hoshigaki, Sasori, Deidara, Hidan and Kakuzu—members of a dreaded shinobi group called the Akatsuki—attacked Konohagakure. Naruto narrowly manages to launch a counter-attack but why have these shinobi appeared when all of them were meant to have died? The mystery remains, but the shinobi are praised by heir families for completing such a dangerous mission. However, one of them who has never known the faces of his parents, Naruto, cannot help but feel lonely. At that exact time, suddenly, the masked man makes his appearance in Konoha. Naruto and his allies are both attacked by the man's mysterious new doujutsu.\n(Source: Naruto Wikia)",
			'description': "Ten years ago, a gigantic demon beast known as the Nine-Tailed Demon Fox was released from its jinchuuriki by an unknown shinobi wearing a mask. The village of Konohagakure was close to destruction by the attack of the Nine-Tails, but the village was saved by its leader. Minato Namikaze and his wife Kushina Uzumaki—who was the jinchuuriki at the time of the attack—sealed away the demon inside their new born son: Naruto Uzumaki. However, this act of saving the village cost them their lives and they left the future of the ninja world to Naruto.\nWith the demon fox sealed away, things continued as normal. However, the peace of the village would not last long, for Pain, Konan, Itachi Uchiha, Kisame Hoshigaki, Sasori, Deidara, Hidan and Kakuzu—members of a dreaded shinobi group called the Akatsuki—attacked Konohagakure. Naruto narrowly manages to launch a counter-attack but why have these shinobi appeared when all of them were meant to have died? The mystery remains, but the shinobi are praised by heir families for completing such a dangerous mission. However, one of them who has never known the faces of his parents, Naruto, cannot help but feel lonely. At that exact time, suddenly, the masked man makes his appearance in Konoha. Naruto and his allies are both attacked by the man's mysterious new doujutsu.\n(Source: Naruto Wikia)",
			'coverImageTopOffset': 100,
			'titles': {
				'en': 'Road to Ninja: Naruto the Movie',
				'en_jp': 'Naruto: Shippuuden Movie 6 - Road to Ninja',
				'en_us': 'Road to Ninja: Naruto the Movie',
				'ja_jp': 'ROAD TO NINJA NARUTO THE MOVIE'
			},
			'canonicalTitle': 'Naruto: Shippuuden Movie 6 - Road to Ninja',
			'abbreviatedTitles': ['Naruto Movie 9'],
			'averageRating': '77.71',
			'ratingFrequencies': {
				'2': '57',
				'3': '0',
				'4': '77',
				'5': '4',
				'6': '105',
				'7': '3',
				'8': '279',
				'9': '4',
				'10': '452',
				'11': '20',
				'12': '985',
				'13': '44',
				'14': '2323',
				'15': '101',
				'16': '2019',
				'17': '79',
				'18': '991',
				'19': '25',
				'20': '2446'
			},
			'userCount': 16513,
			'favoritesCount': 77,
			'startDate': '2012-07-28',
			'endDate': '2012-07-28',
			'nextRelease': None,
			'popularityRank': 697,
			'ratingRank': 1029,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/7008/tiny.jpg?1597697198',
				'small': 'https://media.kitsu.io/anime/poster_images/7008/small.jpg?1597697198',
				'medium': 'https://media.kitsu.io/anime/poster_images/7008/medium.jpg?1597697198',
				'large': 'https://media.kitsu.io/anime/poster_images/7008/large.jpg?1597697198',
				'original': 'https://media.kitsu.io/anime/poster_images/7008/original.jpg?1597697198',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/7008/tiny.jpg?1597702713',
				'small': 'https://media.kitsu.io/anime/cover_images/7008/small.jpg?1597702713',
				'large': 'https://media.kitsu.io/anime/cover_images/7008/large.jpg?1597702713',
				'original': 'https://media.kitsu.io/anime/cover_images/7008/original.jpg?1597702713',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 109,
			'totalLength': 109,
			'youtubeVideoId': 'TDpYU8OmD-k',
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/7008/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/7008/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/7008/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/7008/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/7008/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/7008/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/7008/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/7008/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/7008/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/7008/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/7008/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/7008/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/7008/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/7008/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/7008/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/7008/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/7008/anime-staff'
				}
			}
		}
	}, {
		'id': '6022',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/6022'
		},
		'attributes': {
			'createdAt': '2013-02-20T17:33:08.334Z',
			'updatedAt': '2021-07-01T12:00:04.339Z',
			'slug': 'naruto-x-ut',
			'synopsis': "All-new animation offered throughout UNIQLO clothins stores in Japan on January 1, 2011. The DVD contains an exclusive version of Mayonaka Orchestra, by the Japanese rock band Aqua Timez. A limited number of the DVDs was offered as presents to people who bought UNIQLO's Naruto graphic T-shirts online or in their stores.\n(Source: ANN, edited)",
			'description': "All-new animation offered throughout UNIQLO clothins stores in Japan on January 1, 2011. The DVD contains an exclusive version of Mayonaka Orchestra, by the Japanese rock band Aqua Timez. A limited number of the DVDs was offered as presents to people who bought UNIQLO's Naruto graphic T-shirts online or in their stores.\n(Source: ANN, edited)",
			'coverImageTopOffset': 100,
			'titles': {
				'en_jp': 'Naruto x UT',
				'ja_jp': 'NARUTO×UT'
			},
			'canonicalTitle': 'Naruto x UT',
			'abbreviatedTitles': [],
			'averageRating': '75.42',
			'ratingFrequencies': {
				'2': '32',
				'3': '0',
				'4': '15',
				'5': '0',
				'6': '34',
				'7': '1',
				'8': '72',
				'9': '0',
				'10': '177',
				'11': '3',
				'12': '334',
				'13': '3',
				'14': '525',
				'15': '8',
				'16': '350',
				'17': '3',
				'18': '203',
				'19': '1',
				'20': '586'
			},
			'userCount': 3985,
			'favoritesCount': 18,
			'startDate': '2011-01-01',
			'endDate': '2011-01-01',
			'nextRelease': None,
			'popularityRank': 2360,
			'ratingRank': 1674,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'OVA',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/6022/tiny.jpg?1597699263',
				'small': 'https://media.kitsu.io/anime/poster_images/6022/small.jpg?1597699263',
				'medium': 'https://media.kitsu.io/anime/poster_images/6022/medium.jpg?1597699263',
				'large': 'https://media.kitsu.io/anime/poster_images/6022/large.jpg?1597699263',
				'original': 'https://media.kitsu.io/anime/poster_images/6022/original.jpg?1597699263',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/6022/tiny.jpg?1597701805',
				'small': 'https://media.kitsu.io/anime/cover_images/6022/small.jpg?1597701805',
				'large': 'https://media.kitsu.io/anime/cover_images/6022/large.jpg?1597701805',
				'original': 'https://media.kitsu.io/anime/cover_images/6022/original.jpg?1597701805',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 6,
			'totalLength': 6,
			'youtubeVideoId': None,
			'showType': 'OVA',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/6022/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/6022/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/6022/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/6022/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/6022/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/6022/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/6022/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/6022/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/6022/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/6022/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/6022/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/6022/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/6022/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/6022/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/6022/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/6022/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/6022/anime-staff'
				}
			}
		}
	}, {
		'id': '10089',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/10089'
		},
		'attributes': {
			'createdAt': '2014-12-24T00:39:33.338Z',
			'updatedAt': '2021-07-01T13:46:12.258Z',
			'slug': 'boruto-naruto-the-movie',
			'synopsis': "Boruto Uzumaki has inherited the mischievous spirit and endless energy from his famous father, the 7th Hokage, Naruto. As he enters his Chunin exams, a harsh decision made by Naruto angers Boruto, causing their personalities to clash, awakening a fierce ambition within the young shinobi to surpass his father with his own skills and techniques. But in order to do so, he will need the help of none other than Uchiha Sasuke, Naruto's lifelong rival and childhood friend. Although Boruto has convinced himself that he has what it takes to surpass the 7th Hokage, he soon discovers that the road ahead is not nearly as simple as the young shinobi has envisioned.Boruto: Naruto the Movie opens the doors for a new generation of shinobi to put their abilities to the test, as they face a mysterious enemy and hope to restore peace to Konoha, and the hardships within their own families. The 7th Hokage certainly has an impressive battle history behind him, but on this occasion, he will need the strong teamwork of old friends and new talents in order to win.",
			'description': "Boruto Uzumaki has inherited the mischievous spirit and endless energy from his famous father, the 7th Hokage, Naruto. As he enters his Chunin exams, a harsh decision made by Naruto angers Boruto, causing their personalities to clash, awakening a fierce ambition within the young shinobi to surpass his father with his own skills and techniques. But in order to do so, he will need the help of none other than Uchiha Sasuke, Naruto's lifelong rival and childhood friend. Although Boruto has convinced himself that he has what it takes to surpass the 7th Hokage, he soon discovers that the road ahead is not nearly as simple as the young shinobi has envisioned.Boruto: Naruto the Movie opens the doors for a new generation of shinobi to put their abilities to the test, as they face a mysterious enemy and hope to restore peace to Konoha, and the hardships within their own families. The 7th Hokage certainly has an impressive battle history behind him, but on this occasion, he will need the strong teamwork of old friends and new talents in order to win.",
			'coverImageTopOffset': 145,
			'titles': {
				'en': 'Boruto: Naruto the Movie',
				'en_jp': 'Boruto: Naruto the Movie',
				'en_us': 'Boruto: Naruto the Movie',
				'ja_jp': 'BORUTO -NARUTO THE MOVIE-'
			},
			'canonicalTitle': 'Boruto: Naruto the Movie',
			'abbreviatedTitles': ['Gekijouban Naruto (2015)'],
			'averageRating': '76.94',
			'ratingFrequencies': {
				'2': '130',
				'3': '4',
				'4': '97',
				'5': '7',
				'6': '107',
				'7': '5',
				'8': '484',
				'9': '11',
				'10': '525',
				'11': '28',
				'12': '1172',
				'13': '85',
				'14': '2969',
				'15': '162',
				'16': '2483',
				'17': '148',
				'18': '1360',
				'19': '45',
				'20': '2837'
			},
			'userCount': 19956,
			'favoritesCount': 113,
			'startDate': '2015-08-07',
			'endDate': '2015-08-07',
			'nextRelease': None,
			'popularityRank': 571,
			'ratingRank': 1202,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/10089/tiny.jpg?1597697270',
				'small': 'https://media.kitsu.io/anime/poster_images/10089/small.jpg?1597697270',
				'medium': 'https://media.kitsu.io/anime/poster_images/10089/medium.jpg?1597697270',
				'large': 'https://media.kitsu.io/anime/poster_images/10089/large.jpg?1597697270',
				'original': 'https://media.kitsu.io/anime/poster_images/10089/original.jpg?1597697270',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/10089/tiny.jpg?1597702818',
				'small': 'https://media.kitsu.io/anime/cover_images/10089/small.jpg?1597702818',
				'large': 'https://media.kitsu.io/anime/cover_images/10089/large.jpg?1597702818',
				'original': 'https://media.kitsu.io/anime/cover_images/10089/original.png?1597702818',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 95,
			'totalLength': 95,
			'youtubeVideoId': 'Cvdv2GGnn0A',
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/10089/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/10089/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/10089/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/10089/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/10089/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/10089/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/10089/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/10089/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/10089/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/10089/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/10089/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/10089/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/10089/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/10089/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/10089/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/10089/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/10089/anime-staff'
				}
			}
		}
	}, {
		'id': '13051',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/13051'
		},
		'attributes': {
			'createdAt': '2017-01-22T00:11:34.745Z',
			'updatedAt': '2021-07-01T13:53:57.341Z',
			'slug': 'boruto-naruto-next-generations',
			'synopsis': "Naruto was a young shinobi with an incorrigible knack for mischief. He achieved his dream to become the greatest ninja in the village and his face sits atop the Hokage monument. But this is not his story... A new generation of ninja are ready to take the stage, led by Naruto's own son, Boruto!(Source: VIZ Media)",
			'description': "Naruto was a young shinobi with an incorrigible knack for mischief. He achieved his dream to become the greatest ninja in the village and his face sits atop the Hokage monument. But this is not his story... A new generation of ninja are ready to take the stage, led by Naruto's own son, Boruto!(Source: VIZ Media)",
			'coverImageTopOffset': 0,
			'titles': {
				'en_jp': 'Boruto: Naruto Next Generations',
				'ja_jp': 'BORUTO -NARUTO NEXT GENERATIONS-'
			},
			'canonicalTitle': 'Boruto: Naruto Next Generations',
			'abbreviatedTitles': [],
			'averageRating': '65.16',
			'ratingFrequencies': {
				'2': '649',
				'3': '18',
				'4': '223',
				'5': '22',
				'6': '385',
				'7': '39',
				'8': '1429',
				'9': '51',
				'10': '968',
				'11': '88',
				'12': '1411',
				'13': '158',
				'14': '2613',
				'15': '172',
				'16': '1057',
				'17': '100',
				'18': '437',
				'19': '61',
				'20': '1944'
			},
			'userCount': 41257,
			'favoritesCount': 1058,
			'startDate': '2017-04-05',
			'endDate': None,
			'nextRelease': '2021-07-07T17:55:00.000+09:00',
			'popularityRank': 204,
			'ratingRank': 7090,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'TV',
			'status': 'current',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/13051/tiny.jpg?1624277050',
				'small': 'https://media.kitsu.io/anime/poster_images/13051/small.jpg?1624277050',
				'medium': 'https://media.kitsu.io/anime/poster_images/13051/medium.jpg?1624277050',
				'large': 'https://media.kitsu.io/anime/poster_images/13051/large.jpg?1624277050',
				'original': 'https://media.kitsu.io/anime/poster_images/13051/original.jpg?1624277050',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/13051/tiny.jpg?1601201365',
				'small': 'https://media.kitsu.io/anime/cover_images/13051/small.jpg?1601201365',
				'large': 'https://media.kitsu.io/anime/cover_images/13051/large.jpg?1601201365',
				'original': 'https://media.kitsu.io/anime/cover_images/13051/original.png?1601201365',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': None,
			'episodeLength': 23,
			'totalLength': 5198,
			'youtubeVideoId': 'NnDVX0bc3eI',
			'showType': 'TV',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/13051/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/13051/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/13051/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/13051/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/13051/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/13051/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/13051/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/13051/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/13051/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/13051/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/13051/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/13051/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/13051/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/13051/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/13051/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/13051/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/13051/anime-staff'
				}
			}
		}
	}, {
		'id': '3606',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/3606'
		},
		'attributes': {
			'createdAt': '2013-02-20T16:55:25.720Z',
			'updatedAt': '2021-07-01T13:46:16.034Z',
			'slug': 'naruto-shippuden-movie-2-kizuna',
			'synopsis': 'A mysterious group of ninjas makes a surprise attack on the Konohagakure, which takes great damage. The nightmare of another Shinobi World War could become a reality. Sasuke, who left Konoha to kill his brother, Itachi, appears for the second time in front of Naruto at an unknown location to prevent it from coming to fruition.\n(Source: Wikipedia)',
			'description': 'A mysterious group of ninjas makes a surprise attack on the Konohagakure, which takes great damage. The nightmare of another Shinobi World War could become a reality. Sasuke, who left Konoha to kill his brother, Itachi, appears for the second time in front of Naruto at an unknown location to prevent it from coming to fruition.\n(Source: Wikipedia)',
			'coverImageTopOffset': 100,
			'titles': {
				'en': 'Naruto: Shippuden the Movie 2 -Bonds-',
				'en_jp': 'Naruto: Shippuuden Movie 2 - Kizuna',
				'en_us': 'Naruto: Shippuden the Movie 2 -Bonds-',
				'ja_jp': ' 劇場版NARUTO-ナルト- 疾風伝 絆'
			},
			'canonicalTitle': 'Naruto: Shippuuden Movie 2 - Kizuna',
			'abbreviatedTitles': ['Naruto Movie 5', 'Naruto Shippuuden Movie 2', 'Naruto Shippuuden: Bonds'],
			'averageRating': '71.9',
			'ratingFrequencies': {
				'2': '59',
				'3': '2',
				'4': '84',
				'5': '2',
				'6': '128',
				'7': '3',
				'8': '338',
				'9': '4',
				'10': '641',
				'11': '17',
				'12': '1179',
				'13': '34',
				'14': '2133',
				'15': '50',
				'16': '1444',
				'17': '21',
				'18': '520',
				'19': '9',
				'20': '1134'
			},
			'userCount': 13918,
			'favoritesCount': 34,
			'startDate': '2008-08-02',
			'endDate': '2008-08-02',
			'nextRelease': None,
			'popularityRank': 842,
			'ratingRank': 3155,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/3606/tiny.jpg?1597698083',
				'small': 'https://media.kitsu.io/anime/poster_images/3606/small.jpg?1597698083',
				'medium': 'https://media.kitsu.io/anime/poster_images/3606/medium.jpg?1597698083',
				'large': 'https://media.kitsu.io/anime/poster_images/3606/large.jpg?1597698083',
				'original': 'https://media.kitsu.io/anime/poster_images/3606/original.jpg?1597698083',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/3606/tiny.jpg?1597700972',
				'small': 'https://media.kitsu.io/anime/cover_images/3606/small.jpg?1597700972',
				'large': 'https://media.kitsu.io/anime/cover_images/3606/large.jpg?1597700972',
				'original': 'https://media.kitsu.io/anime/cover_images/3606/original.jpg?1597700972',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 93,
			'totalLength': 93,
			'youtubeVideoId': 'OkI3ZCEbx_E',
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/3606/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/3606/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/3606/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/3606/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/3606/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/3606/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/3606/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/3606/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/3606/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/3606/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/3606/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/3606/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/3606/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/3606/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/3606/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/3606/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/3606/anime-staff'
				}
			}
		}
	}, {
		'id': '833',
		'type': 'anime',
		'links': {
			'self': 'https://kitsu.io/api/edge/anime/833'
		},
		'attributes': {
			'createdAt': '2013-02-20T16:13:20.622Z',
			'updatedAt': '2021-07-01T13:46:15.742Z',
			'slug': 'naruto-movie-2-daigekitotsu-maboroshi-no-chiteiiseki-dattebayo',
			'synopsis': 'Naruto, Shikamaru, and Sakura are executing their mission of delivering a lost pet to a certain village. However, right in the midst of things, troops led by the mysterious knight, Temujin, attack them. In the violent battle, the three become separated. Temujin challenges Naruto to a fight and at the end of the fierce battle, both fall together from a high cliff. Furthermore, Shikamaru, having been left behind, beholds a giant moving fortress as it appears before his very eyes. In order to get a grasp on the situation, he infiltrates the fortress by himself, however once there he witnesses a frightening sight... \n(Source: ANN)',
			'description': 'Naruto, Shikamaru, and Sakura are executing their mission of delivering a lost pet to a certain village. However, right in the midst of things, troops led by the mysterious knight, Temujin, attack them. In the violent battle, the three become separated. Temujin challenges Naruto to a fight and at the end of the fierce battle, both fall together from a high cliff. Furthermore, Shikamaru, having been left behind, beholds a giant moving fortress as it appears before his very eyes. In order to get a grasp on the situation, he infiltrates the fortress by himself, however once there he witnesses a frightening sight... \n(Source: ANN)',
			'coverImageTopOffset': 210,
			'titles': {
				'en': 'Naruto the Movie 2: Legend of the Stone of Gelel',
				'en_jp': 'Naruto Movie 2: Dai Gekitotsu! Maboroshi no Chiteiiseki Dattebayo!',
				'ja_jp': '劇場版\u3000NARUTO\u3000大激突！幻の地底遺跡だってばよ'
			},
			'canonicalTitle': 'Naruto Movie 2: Dai Gekitotsu! Maboroshi no Chiteiiseki Dattebayo!',
			'abbreviatedTitles': ['Naruto THE Movie vol.2', 'Naruto Movie 2', 'Gekijouban Naruto'],
			'averageRating': '66.85',
			'ratingFrequencies': {
				'2': '105',
				'3': '3',
				'4': '137',
				'5': '4',
				'6': '168',
				'7': '5',
				'8': '579',
				'9': '13',
				'10': '1075',
				'11': '11',
				'12': '1496',
				'13': '37',
				'14': '2013',
				'15': '31',
				'16': '1045',
				'17': '22',
				'18': '407',
				'19': '4',
				'20': '818'
			},
			'userCount': 13170,
			'favoritesCount': 23,
			'startDate': '2005-08-06',
			'endDate': '2005-08-06',
			'nextRelease': None,
			'popularityRank': 900,
			'ratingRank': 6048,
			'ageRating': 'PG',
			'ageRatingGuide': 'Teens 13 or older',
			'subtype': 'movie',
			'status': 'finished',
			'tba': None,
			'posterImage': {
				'tiny': 'https://media.kitsu.io/anime/poster_images/833/tiny.jpg?1597698674',
				'small': 'https://media.kitsu.io/anime/poster_images/833/small.jpg?1597698674',
				'medium': 'https://media.kitsu.io/anime/poster_images/833/medium.jpg?1597698674',
				'large': 'https://media.kitsu.io/anime/poster_images/833/large.jpg?1597698674',
				'original': 'https://media.kitsu.io/anime/poster_images/833/original.jpg?1597698674',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 110,
							'height': 156
						},
						'small': {
							'width': 284,
							'height': 402
						},
						'medium': {
							'width': 390,
							'height': 554
						},
						'large': {
							'width': 550,
							'height': 780
						}
					}
				}
			},
			'coverImage': {
				'tiny': 'https://media.kitsu.io/anime/cover_images/833/tiny.jpg?1597702114',
				'small': 'https://media.kitsu.io/anime/cover_images/833/small.jpg?1597702114',
				'large': 'https://media.kitsu.io/anime/cover_images/833/large.jpg?1597702114',
				'original': 'https://media.kitsu.io/anime/cover_images/833/original.jpg?1597702114',
				'meta': {
					'dimensions': {
						'tiny': {
							'width': 840,
							'height': 200
						},
						'small': {
							'width': 1680,
							'height': 400
						},
						'large': {
							'width': 3360,
							'height': 800
						}
					}
				}
			},
			'episodeCount': 1,
			'episodeLength': 96,
			'totalLength': 96,
			'youtubeVideoId': None,
			'showType': 'movie',
			'nsfw': False
		},
		'relationships': {
			'genres': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/genres',
					'related': 'https://kitsu.io/api/edge/anime/833/genres'
				}
			},
			'categories': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/categories',
					'related': 'https://kitsu.io/api/edge/anime/833/categories'
				}
			},
			'castings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/castings',
					'related': 'https://kitsu.io/api/edge/anime/833/castings'
				}
			},
			'installments': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/installments',
					'related': 'https://kitsu.io/api/edge/anime/833/installments'
				}
			},
			'mappings': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/mappings',
					'related': 'https://kitsu.io/api/edge/anime/833/mappings'
				}
			},
			'reviews': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/reviews',
					'related': 'https://kitsu.io/api/edge/anime/833/reviews'
				}
			},
			'mediaRelationships': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/media-relationships',
					'related': 'https://kitsu.io/api/edge/anime/833/media-relationships'
				}
			},
			'characters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/characters',
					'related': 'https://kitsu.io/api/edge/anime/833/characters'
				}
			},
			'staff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/staff',
					'related': 'https://kitsu.io/api/edge/anime/833/staff'
				}
			},
			'productions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/productions',
					'related': 'https://kitsu.io/api/edge/anime/833/productions'
				}
			},
			'quotes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/quotes',
					'related': 'https://kitsu.io/api/edge/anime/833/quotes'
				}
			},
			'episodes': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/episodes',
					'related': 'https://kitsu.io/api/edge/anime/833/episodes'
				}
			},
			'streamingLinks': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/streaming-links',
					'related': 'https://kitsu.io/api/edge/anime/833/streaming-links'
				}
			},
			'animeProductions': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/anime-productions',
					'related': 'https://kitsu.io/api/edge/anime/833/anime-productions'
				}
			},
			'animeCharacters': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/anime-characters',
					'related': 'https://kitsu.io/api/edge/anime/833/anime-characters'
				}
			},
			'animeStaff': {
				'links': {
					'self': 'https://kitsu.io/api/edge/anime/833/relationships/anime-staff',
					'related': 'https://kitsu.io/api/edge/anime/833/anime-staff'
				}
			}
		}
	}],
	'meta': {
		'count': 466
	},
	'links': {
		'first': 'https://kitsu.io/api/edge/anime?filter%5Btext%5D=Naruto+&page%5Blimit%5D=10&page%5Boffset%5D=0',
		'next': 'https://kitsu.io/api/edge/anime?filter%5Btext%5D=Naruto+&page%5Blimit%5D=10&page%5Boffset%5D=10',
		'last': 'https://kitsu.io/api/edge/anime?filter%5Btext%5D=Naruto+&page%5Blimit%5D=10&page%5Boffset%5D=456'
	}
}
```

