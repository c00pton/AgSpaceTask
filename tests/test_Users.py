from . import BASE_ADDRESS, fake, get, post, put, delete
from agspace import models, schemas
import random


BASE_URL = '/users'
BASE_DB = models.User
BASE_MODEL = schemas.User


def user_profile_gen():
    profile = fake.profile()
    return {
        'first_name': profile['name'].split()[0],
        'last_name': profile['name'].split()[1],
        'email': profile['mail'],
        'address': {
            'address': profile['address']
        },
        'account': {
            'status': 'active'
        },
        'password_hash': fake.password(),
        'is_active': bool(round(random.random()))
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
    try:
        assert code == 200
    except AssertionError:
        print(code, res)
    return res


def update_password_hash(id: int, data: dict):
    code, res = put(f'{BASE_URL}/{id}/password_hash', data)
    assert code == 200
    return res


def delete_user(id: int):
    code, d = delete(f'{BASE_URL}', id)
    assert (code, d) == (200, {'deleted': True})
    assert None == get_one(id)


def test_user_lifecycle():
    # Create a user from a base profile
    user_data = user_profile_gen()
    user = create(user_data)
    del user_data['account']
    del user_data['address']
    # Update some details
    user = update_password_hash(user['id'], {'password_hash': fake.password()})
    user['is_active'] = not user['is_active']
    user = update(user['id'], user)
    user['id'] = user['id']
    user['first_name'] = fake.first_name()
    user['last_name'] = fake.last_name()
    user = update(user['id'], user)
    # # Delete the user
    delete_user(user['id'])
