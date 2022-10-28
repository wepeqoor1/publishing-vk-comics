import os
import random

from dotenv import load_dotenv

from vk_api import (
    get_address_for_upload_photo,
    upload_photo_to_server,
    save_photo_in_album_group,
    publish_comic_on_wall
)
from xkcd_api import download_comic_img, get_comic_data, get_count_comics

COMIC_IMG_NAME = 'comic.png'


def main():
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    vk_group_id = os.getenv('VK_GROUP_ID')

    count_comics = get_count_comics()
    random_comic = random.randint(1, count_comics)

    comics_description = get_comic_data(comic_number=random_comic)
    comic_img, comic_comment = comics_description['img'], comics_description['alt']
    download_comic_img(url=comic_img)

    upload_url = get_address_for_upload_photo(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
    )
    if not upload_url:
        print('Не удалось получить адрес загрузки фото')
        exit(0)

    data_upload_photo = upload_photo_to_server(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        upload_url=upload_url,
    )
    server, photo, hash_ = data_upload_photo['server'], data_upload_photo['photo'], data_upload_photo['hash']

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

    os.remove(COMIC_IMG_NAME)


if __name__ == '__main__':
    load_dotenv()
    main()
