import os

import requests
from dotenv import load_dotenv

from vk_api import (
    get_address_for_download_photo,
    upload_photo_to_server,
    save_photo_in_albom_group,
    publish_in_wall_group
)

VERSION_API = 5.131


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


def main():
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_APP_ID')

    comics_description = get_comic_data(comic_number=64)
    comic_img = comics_description['img']
    download_comic_img(url=comic_img)
    # comic_comment = comics_description['alt']
    address_photo = get_address_for_download_photo(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        version_api=VERSION_API
    )
    print(address_photo)


if __name__ == '__main__':
    load_dotenv()
    main()
