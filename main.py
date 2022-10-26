import os

import requests
from dotenv import load_dotenv


def get_upload_url_group_vk(access_token: str) -> None:
    pass
=======
    with open(file_name, 'wb') as file:
        file.write(response.content)
>>>>>>> 67de17ad807885647ce3fc5c2043b34ce7d68f29


def main():
    vk_access_token = os.getenv('VK_APP_CODE')
=======
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
    upload_url_photo = get_address_for_upload_photo(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        version_api=VERSION_API
    )
    print(upload_url_photo)
    data_from_upload_photo = upload_photo_to_server(
        vk_access_token=vk_access_token,
        vk_group_id=vk_group_id,
        version_api=VERSION_API,
        img_name=COMIC_IMG_NAME
    )
    print(data_from_upload_photo)


if __name__ == '__main__':
    load_dotenv()
    main()
