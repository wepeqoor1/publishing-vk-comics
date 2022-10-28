import requests


VK_VERSION_API = 5.131
COMIC_IMG_NAME = 'comic.png'


def get_address_for_upload_photo(vk_access_token: str, vk_group_id: str) -> str | None:
    """Получает адресс для загрузки фото"""
    url = f'https://api.vk.com/method/photos.getWallUploadServer/'
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'v': VK_VERSION_API
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json().get('response')['upload_url']


def upload_photo_to_server(vk_access_token: str, vk_group_id: str, upload_url: str) -> dict:
    """Загружает фото на сервер"""
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'v': VK_VERSION_API
    }

    with open(COMIC_IMG_NAME, 'rb') as image:
        files = {
            'photo': image
        }
        response = requests.post(upload_url, params=params, files=files)
        response.raise_for_status()
        return response.json()


def save_photo_in_album_group(vk_group_id: str, vk_access_token: str, photo: str, server: str, hash_: str) -> str:
    """
    Сохраняет картинку в альбоме группы ВК
    """
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'access_token': vk_access_token,
        'group_id': vk_group_id,
        'server': server,
        'photo': photo,
        'hash': hash_,
        'v': VK_VERSION_API
    }

    response = requests.post(url=url, params=params)
    response.raise_for_status()
    api_response = response.json()

    owner_id = api_response['response'][0]['owner_id']
    media_id = api_response['response'][0]['id']

    attachment = f'photo{owner_id}_{media_id}'

    return attachment


def publish_comic_on_wall(vk_group_id: str, vk_access_token: str, message: str, attachments: str) -> requests.Response:
    """
    Публикуем комикс на стене сообзества
    """
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': vk_access_token,
        'message': message,
        'owner_id': f'-{vk_group_id}',
        'from_group': 1,
        'attachments': attachments,
        'v': VK_VERSION_API
    }

    response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response
