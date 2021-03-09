from . import BASE_ADDRESS, fake, get, post, put, delete
from agspace import models, schemas


BASE_URL = '/address'
BASE_DB = models.Address
BASE_MODEL = schemas.Address


def address_profile_gen():
    return {
        'address': fake.address()
    }


def get_all():
    code, res_list = get(BASE_URL)
    assert code == 200
    assert isinstance(res_list, list)
    return res_list


def get_one(id: int):
    code, res = get(f'{BASE_URL}/{id}')
    assert code == 200
    return res


def create(data: dict):
    code, res = post(BASE_URL, data)
    assert code == 200
    return res


def update(id: int, data: dict):
    code, res = put(f'{BASE_URL}/{id}', data)
    assert code == 200
    for k, v in data.items():
        if k in res:
            assert res[k] == v
    return res


def delete_address(id: int):
    code, d = delete(f'{BASE_URL}', id)
    assert (code, d) == (200, {'deleted': True})
    assert None == get_one(id)


def test_address_lifecycle():
    # Create address from base profile
    address_data = address_profile_gen()
    address = create(address_data)
    address_data['id'] = address['id']
    address_data['address'] = fake.address()
    address = update(address_data['id'], address_data)
    delete_address(address_data['id'])
