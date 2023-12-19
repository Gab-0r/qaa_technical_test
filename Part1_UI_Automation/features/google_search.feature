Feature: Google Search
  As a user
  I want to make a Google search

  Background: The user search by keyword
    Given The user is on the Google homepage
    When The user type test automation into the search field and clicks on the Google search button

  @scenario1
  Scenario: The user can search with Google Search
    Then The user goes to the search results page,and the first 3 results contain the word automation

  @scenario2
  Scenario: The user can go to the first result search
    When The user clicks on the first result link
    Then The user goes to the page, and the page title contains the word automation