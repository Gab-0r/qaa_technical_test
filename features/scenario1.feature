Feature: scenario1
  As a user
  I want to make a Google search

  Scenario: Search 'test automation' with Google search
    Given The user is on the Google homepage
    When The user type test automation into the search field and clicks on the Google search button
    Then The user goes to the search results page,and the first 3 results contain the word automation

