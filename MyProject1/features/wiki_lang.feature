Feature: Validating Inputs

  Scenario: Sign Up Page
    Given The User is on the Sign Up Home Page
    When User enters First Name as <firstName>
    When User enters Last Name as <lastName>
    When User enters Email as <email>
    When User enters Address as <address>
    When User enters Phone Number as <phoneNumber>
    When User puts UserName as <userName>
    When User puts PassWord as <passWord>
    When the user presses on Sign Up button
    Then The User is able to signe up successfully.


  Scenario: Login Page Works
    Given The User is on the Login Home Page
    When User enters Username as <username>
    When User enters Password as <password>
    When User clicks on login button
    When the user clicks on logout button
    Then User is able to successfully login to the Login Home Page.


  Scenario: Filling Reimbursement Page
    Given The User is on the Reimbursement Home Page
    When User enters Event Location as <location>
    When User enters Event Type as <type>
    When User enters Event Description as <description>
    When User enters Event Justification as <justification>
    When User enters Event Cost as <cost>
    When User enters Grade Format as <grade>
    When User enters Employee ID as <id>
    When User enters Lateness as <late>
    When User clicks on Courses as <course>
    When the user clicks on Sign Up button
    Then User is able to successfully signed up.

  Scenario: Getting A new Course Works
    Given The User is on the Login Page
    When User enters clicks on the course dropdown
    When User clicks on Get New Course Button
    Then The course is successfully added.


  Scenario: Approving an Employee
    Given The User is on the Management Home Page
    When User enters an employee id
    When User clicks on Get Employee Info button
    When User click on approve button
    When User click on Get Employee Info Btn
    Then The employee is successfully approved.

  Scenario: Rejecting an Employee
    Given The User is on the Management Page
    When User puts an employee id
    When User presses on Get Employee Info button
    When User clicks on reject button
    When User presses on Get Employee Info Btn
    Then The employee is successfully rejected.
