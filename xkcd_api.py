from typing import NamedTuple

import requests


class ComicData(NamedTuple):
    img_url: str
    comment: str


def get_comic_data() -> ComicData:
    # Получаем номер последнего комикса
    last_comic_url = f"https://xkcd.com/info.0.json"
    response = requests.get(last_comic_url)
    response.raise_for_status()
    last_comic = response.json()['num']

    # Получаем данные по конкретному комиксу
    url = f"https://xkcd.com/{last_comic}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    comic = response.json()

    return ComicData(img_url=comic['img'], comment=comic['alt'])


def download_comic_img(url: str) -> None:
    file_name = 'comic.png'
    response = requests.get(url)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response.content)
