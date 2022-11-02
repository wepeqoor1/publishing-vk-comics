import os

import requests
from dotenv import load_dotenv

from vk_api import (
    get_address_for_upload_photo,
    upload_photo_to_server,
    save_photo_in_album_group,
    publish_comic_on_wall
)
from xkcd_api import get_image_link_and_description_comic

COMIC_IMG_NAME = 'comic.png'


def download_img(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    with open(COMIC_IMG_NAME, 'wb') as file:
        file.write(response.content)


def main():
    load_dotenv()

    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')

    comic_img_url, comic_comment = get_image_link_and_description_comic()

    upload_url = get_address_for_upload_photo(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
    )
    if not upload_url:
        print('Не удалось получить адрес загрузки фото')

    try:
        download_img(url=comic_img_url)
        server, photo, hash_ = upload_photo_to_server(
            vk_access_token=vk_access_token,
            vk_group_id=vk_group_id,
            upload_url=upload_url,
        )
    finally:
        os.remove(COMIC_IMG_NAME)

    attachment = save_photo_in_album_group(
        vk_group_id=vk_group_id, vk_access_token=vk_access_token,
        photo=photo, server=server, hash_=hash_
    )

    publish_comic_on_wall(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        message=comic_comment,
        attachments=attachment
    )


if __name__ == '__main__':
    main()
