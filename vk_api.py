import requests

from utils import get_comic_img


def get_address_for_upload_photo(vk_access_token: str, vk_group_id: str, version_api: float) -> dict:
    """Получает адресс для загрузки фото"""
    method = 'photos.getWallUploadServer'
    url = f'https://api.vk.com/method/{method}/'
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'v': version_api
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def upload_photo_to_server(vk_access_token: str, vk_group_id: str, version_api: float, img_name: str) -> dict:
    """Загружает фото на сервер"""
    method = 'photos.saveWallPhoto'
    url = f'https://api.vk.com/method/{method}/'
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'v': version_api
    }

    with open(img_name, 'rb') as image:
        files = {
            'photo': image
        }
    response = requests.post(url, params=params, files=files)
    response.raise_for_status()
    return response.json()


def save_photo_in_album_group():
    """Сохраняет фото в альбоме группы"""
    pass


def publish_in_wall_group():
    """Публикует зхаписи в группе"""
    pass
