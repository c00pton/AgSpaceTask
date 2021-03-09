import json
import requests
from faker import Faker


BASE_ADDRESS = 'http://127.0.0.1:8000'
fake = Faker()


def _url(url: str):
    if BASE_ADDRESS in url:
        url = url.replace(BASE_ADDRESS, '')
    if url.startswith('/'):
        url = url[1:]
    return f'{BASE_ADDRESS}/{url}'


def _resp(response):
    try:
        code = response.status_code
        content = response.content.decode()
        return code, json.loads(content)
    except Exception as e:
        return code, content


def get(url: str):
    res = requests.get(_url(url))
    return _resp(res)


def post(url: str, data: dict):
    res = requests.post(_url(url), data=json.dumps(data))
    return _resp(res)


def put(url: str, data: dict):
    res = requests.put(_url(url), data=json.dumps(data))
    return _resp(res)


def delete(url: str, id: int):
    res = requests.delete(f'{_url(url)}/{id}')
    return _resp(res)
