# Created by sandeepkuri at 2020-01-18
Feature: Perform upload and download
  As a User, I want to upload a file to google drive,
  so that it can be available for others


  Background:
    Given User is on google drive page
    And User is already logged in


  Scenario: uploading file
    When User is clicking on new
    And User is clicking on "file upload" and uploading the file
    # Then user can see the file on the screen


  Scenario: dowloading file
    When user is clicking on file to download
    # Then the file is download in the system