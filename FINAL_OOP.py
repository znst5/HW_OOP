import requests
from pprint import pprint
import json


text = input('Введите сюда текст для картинки: ')
tok = input('Сюда токен с яндекс, если он у вас есть: ')
url = f'https://cataas.com/cat/says/{text}?json=true'
response = requests.get(url)
image = requests.get(response.json()['url'])
image_cat = image.content
pprint(response.json())


params = {
     'path': 'PYAPI-132'
 }
headers = {'Authorization': f'OAuth {tok}'}
response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                        headers=headers,
                        params=params)

params = {
    'path': f'PYAPI-132/{text}'
 }
response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                        headers=headers,
                        params=params)
upload_link = response.json()['href']

requests.put(upload_link, files={'file': image_cat})


