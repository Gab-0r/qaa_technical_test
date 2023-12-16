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