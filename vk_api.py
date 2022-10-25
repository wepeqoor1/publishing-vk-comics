import requests


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
    print(response.url)
    response.raise_for_status()
    return response.json()


def upload_photo_to_server():
    """Загружает фото на сервер"""
    pass


def save_photo_in_albom_group():
    """Сохраняет фото в альбоме группы"""
    pass


def publish_in_wall_group():
    """Публикует зхаписи в группе"""
    pass