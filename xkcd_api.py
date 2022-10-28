import requests


def get_count_comics() -> int:
    url = f"https://xkcd.com/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()['num']


def get_comic_data(comic_number: int) -> dict:
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def download_comic_img(url: str) -> None:
    file_name = 'comic.png'
    response = requests.get(url)
    response.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response.content)
