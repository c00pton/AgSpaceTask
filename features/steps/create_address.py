from behave import *
from tests.test_Address import address_profile_gen, create


@given('we have address details')
def step_impl(context):
    context.address_details = address_profile_gen()


@when('we create the address')
def step_impl(context):
    context.address = create(context.address_details)


@then('confirm address')
def step_impl(context):
    assert context.address['address'] == context.address_details['address']
