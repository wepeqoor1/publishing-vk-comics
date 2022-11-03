import random

import requests


def download_random_comic(image_name: str) -> str:
    last_comic_url = f"https://xkcd.com/info.0.json"
    response = requests.get(last_comic_url)
    response.raise_for_status()
    last_comic = response.json()['num']
    random_comic = random.randint(1, last_comic)

    url_current_comic = f"https://xkcd.com/{random_comic}/info.0.json"
    response = requests.get(url_current_comic)
    response.raise_for_status()
    comic = response.json()

    response = requests.get(comic['img'])
    response.raise_for_status()
    with open(image_name, 'wb') as file:
        file.write(response.content)

    return comic['alt']
