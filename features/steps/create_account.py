from behave import *
from tests.test_Accounts import account_profile_gen, create


@given('we have account details')
def step_impl(context):
    context.account_details = account_profile_gen()


@when('we create the account')
def step_impl(context):
    context.account = create(context.account_details)


@then('confirm account status')
def step_impl(context):
    assert context.account['status'] == context.account_details['status']
