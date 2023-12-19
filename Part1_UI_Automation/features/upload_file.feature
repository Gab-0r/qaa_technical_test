Feature: User can upload files
  As a user
  I want to upload a file

  @scenario4
  Scenario: The user uploads a file correctly
    Given The user is on the upload file page
    When The user attach a file
    And Clicks on upload button
    Then The file is uploaded successfully