Feature: User lifecycle

    Scenario: Create a user
        Given user details
        When we create the user
        Then confirm user address
        And confirm user account status

    Scenario: Create another user
        Given user details
        When we create the user
        Then confirm user address
        And confirm user account status
    
    Scenario: Update the user
        Given a user
        When we update the user email
        Then confirm the user email
    
    Scenario: Delete the user
        Given a user
        When we delete the user
        Then confirm the user was deleted
