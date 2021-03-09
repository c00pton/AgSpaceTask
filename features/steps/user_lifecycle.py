from behave import *
from tests.test_Users import (
    user_profile_gen, create, update, delete_user, get_one)
from tests import fake


EMAIL = fake.email()


@given('user details')
def step_impl(context):
    context.user_details = user_profile_gen()


@when('we create the user')
def step_impl(context):
    context.user = create(context.user_details)


@then('confirm user address')
def step_impl(context):
    assert context.user['address']['address'] is not None

@then('confirm user account status')
def step_impl(context):
    assert context.user['account']['status'] is not None


@given('a user')
def step_impl(context):
    try:
        context.user is not None
    except AttributeError:
        context.user_details = user_profile_gen()
        context.user = create(context.user_details)


@when('we update the user email')
def step_impl(context):
    user_data = context.user.copy()
    user_data['id'] = context.user['id']
    user_data['email'] = EMAIL
    context.user = update(user_data['id'], user_data)


@then('confirm the user email')
def step_impl(context):
    try:
        assert context.user['email'] == EMAIL
    except AssertionError:
        print(context.user)
        raise


@when('we delete the user')
def step_impl(context):
    print(f'Deleting {context.user["id"]}')
    delete_user(context.user['id'])


@then('confirm the user was deleted')
def step_impl(context):
    assert get_one(context.user['id']) == None
