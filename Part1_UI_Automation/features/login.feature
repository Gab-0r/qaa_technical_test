Feature: User can login
  As a user
  I want to login in the page

  @scenario3
  Scenario: The user can login
    Given The user is on the login page
    When The user enters its username and password
    And Clicks on login button
    Then The user has logged successfully
    And The correct login message displayed is the expected

  @scenario3.1
  Scenario Outline: The user logins with invalid username <username>
    Given The user is on the login page
    When The user enters a invalid username <username>
    And Enters a correct password
    Then Clicks on login button
    And The incorrect username message displayed is the expected

    Examples:
      | username  |
      | user1     |
      | user_     |
      | tomsm     |


  @scenario3.2
  Scenario Outline: The user logins with invalid password <password>
    Given The user is on the login page
    When The user enters an invalid password <password>
    And Enters a correct username
    Then Clicks on login button
    And The incorrect password message displayed is the expected

    Examples:
    | password  |
    | pass1 |
    | 1234  |
    | secretpassword  |