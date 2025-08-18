import requests
from pprint import pprint
import json
from yan_token import tok

text = input()
url = f'https://cataas.com/cat/says/{text}'
response = requests.get(url)
image_cat = response.content



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


