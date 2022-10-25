import json
import os

import requests
from dotenv import load_dotenv

from itertools import count


def download_image(url) -> requests.Response:
    response: requests.Response = requests.get(url)
    response.raise_for_status()
    return response


def get_comics_description(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response: requests.Response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_groups_description_vk(access_token: str) -> dict:
    params = {
        'access_token': access_token,
        'extended': 1,  # Full group description
        'v': 5.131,  # API version
    }
    url = f'https://api.vk.com/method/groups.get'
    response: requests.Response = requests.get(url=url, params=params)
    response.raise_for_status()
    return response.json()


def get_upload_url_group_vk(access_token: str) -> None:
    pass


def main():
    vk_access_token = os.getenv('VK_ACCESS_TOKEN')
    for comics_number in count(1):
        # comics_description = get_comics_description(comics_number)
        # comics_img = download_image(comics_description['img'])
        # author_comment = comics_description['alt']
        groups_description = get_groups_description_vk(access_token=vk_access_token)
        with open('vk.json', 'w', encoding='utf-8') as write_file:
            json.dump(groups_description, write_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    load_dotenv()
    main()
