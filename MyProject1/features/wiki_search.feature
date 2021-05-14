Feature: The Login Input Feature Works

  Scenario Outline: Searching for matched username and passwords
    Given The User is on the Login Home Page
    When the User enters Username as <username>
    When the User enters Password as <password>
    When the User clicks on login button
    When the User is able to successfully login to the Login Home Page.
    Then The title should be <title>

  Examples:
    |   username  |password|    title  |
    |   serene    | 1234   | LOGIN FORM|
    |   helen     | 1234  | LOGIN FORM|
    |   aliou     | 12345  | LOGIN FORM|





