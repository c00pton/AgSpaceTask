from . import BASE_ADDRESS, fake, get, post, put, delete
from agspace import models, schemas
import random


BASE_URL = '/accounts'
BASE_DB = models.Account
BASE_MODEL = schemas.Account

STATUSES = ('active', 'inactive', 'suspended')


def account_profile_gen():
    i = random.randint(0, 2)
    return {
        'status': STATUSES[i]
    }


def get_all():
    code, res_list = get(f'{BASE_URL}')
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


def delete_account(id: int):
    code, d = delete(f'{BASE_URL}', id)
    assert (code, d) == (200, {'deleted': True})
    assert None == get_one(id)


def test_account_lifecycle():
    # Create account from base profile
    account_data = account_profile_gen()
    account = create(account_data)
    # Retrieve the id
    account_data['id'] = account['id']
    # Update status
    account_data['status'] = [
        s for s in STATUSES if s != account_data['status']][0]
    account = update(account_data['id'], account_data)
    # Delete the account
    delete_account(account_data['id'])
