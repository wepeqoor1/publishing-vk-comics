import os

import requests
from dotenv import load_dotenv

from vk_api import (
    get_address_for_upload_photo,
    upload_photo_to_server,
    save_photo_in_album_group,
    publish_in_wall_group
)
from xkcd_api import download_comic_img, get_comic_data

VERSION_API = 5.131
COMIC_IMG_NAME = 'comic.png'


def main():
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_APP_ID')

    comics_description = get_comic_data(comic_number=64)
    comic_img = comics_description['img']
    download_comic_img(url=comic_img)
    # comic_comment = comics_description['alt']
    upload_url = get_address_for_upload_photo(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        version_api=VERSION_API
    )
    if not upload_url:
        print('Не удалось получить адрес загрузки фото')
        exit(0)

    print(upload_url)
    data_from_upload_photo = upload_photo_to_server(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        version_api=VERSION_API,
        img_name=COMIC_IMG_NAME,
        upload_url=upload_url,
    )
    print(data_from_upload_photo)


if __name__ == '__main__':
    load_dotenv()
    main()
