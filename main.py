import os

import requests
from dotenv import load_dotenv


def get_comic_data(comic_number: int) -> dict:
    url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def download_comic_img(url: str) -> None:
    file_name = 'comic.png'
    response = requests.get(url)
    response.raise_for_status()
<<<<<<< HEAD
    return response.json()


def get_upload_url_group_vk(access_token: str) -> None:
    pass
=======
    with open(file_name, 'wb') as file:
        file.write(response.content)
>>>>>>> 67de17ad807885647ce3fc5c2043b34ce7d68f29


def main():
    vk_access_token = os.getenv('VK_APP_CODE')
    vk_group_id = os.getenv('VK_APP_ID')

    comics_description = get_comic_data(comic_number=64)
    comic_img = comics_description['img']
    download_comic_img(url=comic_img)
    comic_comment = comics_description['alt']
    print(comic_comment)


if __name__ == '__main__':
    load_dotenv()
    main()
