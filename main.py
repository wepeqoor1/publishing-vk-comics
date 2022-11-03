import os

from dotenv import load_dotenv

from vk_api import (
    get_address_for_upload_photo,
    upload_photo_to_server,
    save_photo_in_album_group,
    publish_comic_on_wall
)
from xkcd_api import download_random_comic

COMIC_IMG_NAME = 'comic.png'


def main():
    load_dotenv()

    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')

    upload_url = get_address_for_upload_photo(
        vk_access_token,
        vk_group_id,
    )
    if not upload_url:
        print('Не удалось получить адрес загрузки фото')

    try:
        comic_comment = download_random_comic(COMIC_IMG_NAME)
        server, photo, hash_ = upload_photo_to_server(
            vk_access_token,
            vk_group_id,
            upload_url,
        )
    finally:
        os.remove(COMIC_IMG_NAME)

    attachment = save_photo_in_album_group(
        vk_group_id,
        vk_access_token,
        photo,
        server,
        hash_
    )

    publish_comic_on_wall(
        vk_access_token,
        vk_group_id,
        comic_comment,
        attachment
    )
    print('Запись опубликована на стене')


if __name__ == '__main__':
    main()
