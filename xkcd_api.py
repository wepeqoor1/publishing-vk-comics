import random
from typing import NamedTuple

import requests


def get_last_comic() -> tuple:
    last_comic_url = f"https://xkcd.com/info.0.json"
    response = requests.get(last_comic_url)
    response.raise_for_status()
    last_comic = response.json()['num']
    random_comic = random.randint(1, last_comic)

    url_current_comic = f"https://xkcd.com/{random_comic}/info.0.json"
    response = requests.get(url_current_comic)
    response.raise_for_status()
    comic = response.json()

    return comic['img'], comic['alt']
