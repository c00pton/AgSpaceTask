Feature: Creating an account

    Scenario: create an account
        Given we have account details
        When we create the account
        Then confirm account status