from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# SIGN UP FORM #########################################################################
@given(u'The User is on the Sign Up Home Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/signup.html")
    sleep(3)


@when(u'User enters First Name as <firstName>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'first_name')))
    driver.find_element_by_id('first_name').send_keys("Ahmadou")
    sleep(3)


@when(u'User enters Last Name as <lastName>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'last_name')))
    driver.find_element_by_id('last_name').send_keys("Samb")
    sleep(3)


@when(u'User enters Email as <email>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email_address')))
    driver.find_element_by_id('email_address').send_keys("ahmadou@gmail.com")
    sleep(3)


@when(u'User enters Address as <address>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'address')))
    driver.find_element_by_id('address').send_keys("5911 Pineglen Court")
    sleep(3)


@when(u'User enters Phone Number as <phoneNumber>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'phone_number')))
    driver.find_element_by_id('phone_number').send_keys("912-342-4532")
    sleep(3)


@when(u'User puts UserName as <userName>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("ahmadou")
    sleep(3)


@when(u'User puts PassWord as <passWord>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("1234")
    sleep(3)


@when(u'the user presses on Sign Up button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'btnsubmit')))
    driver.find_element_by_id('btnsubmit').send_keys(Keys.ENTER)


@then(u'The User is able to signe up successfully.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logout')))
    driver.find_element_by_id('logout').click()
    sleep(3)


# LOGIN FORM ######################################################################
@given(u'The User is on the Login Home Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/login.html")
    sleep(3)


@when(u'User enters Username as <username>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'username')))
    driver.find_element_by_id('username').send_keys("serene")
    sleep(5)


@when(u'User enters Password as <Password>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password')))
    driver.find_element_by_id('password').send_keys("12345")
    sleep(5)


@when(u'User clicks on login button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logbtn')))
    driver.find_element_by_id('logbtn').send_keys(Keys.ENTER)
    sleep(10)


@when(u'the user clicks on logout button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Logout')))
    driver.find_element_by_link_text('Logout').send_keys(Keys.ENTER)
    sleep(10)


@then(u'User is able to successfully login to the Login Home Page.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Login Page')))
    driver.find_element_by_link_text('Login Page').click()


@when(u'the User enters Username as serene')
def step_impl(context):
    pass


@when(u'the User enters Password as 1234')
def step_impl(context):
    pass


@when(u'the User clicks on login button')
def step_impl(context):
    pass


@when(u'the User is able to successfully login to the Login Home Page.')
def step_impl(context):
    pass


@then(u'The title should be LOGIN FORM')
def step_impl(context):
    pass


@when(u'the User enters Username as helen')
def step_impl(context):
    pass


# @when(u'the User enters Password as 1234')
# def step_impl(context):
#     pass


@when(u'the User enters Username as aliou')
def step_impl(context):
    pass

@when(u'the User enters Password as 12345')
def step_impl(context):
    pass

# REIMBURSEMENT FORM ######################################################################

@given(u'The User is on the Reimbursement Home Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/reimbursementform.html")
    sleep(3)


@when(u'User enters Event Location as <location>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'event_location')))
    driver.find_element_by_id('event_location').send_keys("New Jersey")
    sleep(3)


@when(u'User enters Event Type as <type>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'event_type')))
    driver.find_element_by_id('event_type').send_keys("Certified")
    sleep(3)


@when(u'User enters Event Description as <description>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'descrip_tion')))
    driver.find_element_by_id('descrip_tion').send_keys("Good Job")
    sleep(3)


@when(u'User enters Event Justification as <justification>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Justi_fication')))
    driver.find_element_by_id('Justi_fication').send_keys("No Justification Needed")
    sleep(3)


@when(u'User enters Event Cost as <cost>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'event_cost')))
    driver.find_element_by_id('event_cost').send_keys("1000")
    sleep(3)


@when(u'User enters Grade Format as <grade>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'grade_format')))
    driver.find_element_by_id('grade_format').send_keys("A+")
    sleep(3)


@when(u'User enters Employee ID as <id>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'employee_id')))
    driver.find_element_by_id('employee_id').send_keys("80")
    sleep(3)


@when(u'User enters Lateness as <late>')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'is_late')))
    driver.find_element_by_id('is_late').send_keys("True")
    sleep(3)


@when(u'User clicks on Courses as <course>')
def step_impl(context):
    driver: WebDriver = context.driver
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'reimbursementtype'))))
    select.select_by_visible_text('Technical Training')
    sleep(3)


@when(u'the user clicks on Sign Up button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'signUpBtn')))
    driver.find_element_by_id('signUpBtn').send_keys(Keys.ENTER)


@then(u'User is able to successfully signed up.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logout')))
    driver.find_element_by_id('logout').click()
    sleep(3)



# Getting New Course ###################################################################
@given(u'The User is on the Login Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/login.html")
    sleep(3)


@when(u'User enters clicks on the course dropdown')
def step_impl(context):
    driver: WebDriver = context.driver
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'course_name'))))
    select.select_by_visible_text('Seminars')
    sleep(3)


@when(u'User clicks on Get New Course Button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'createbtn')))
    driver.find_element_by_id('createbtn').send_keys(Keys.ENTER)
    sleep(2)


@then(u'The course is successfully added.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logout')))
    driver.find_element_by_id('logout').click()
    sleep(3)


# Approval ###########################################################################
@given(u'The User is on the Management Home Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/management.html")
    sleep(3)


@when(u'User enters an employee id')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'employeeId')))
    driver.find_element_by_id('employeeId').send_keys("80")
    sleep(3)


@when(u'User clicks on Get Employee Info button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'getEmpInfo')))
    driver.find_element_by_id('getEmpInfo').send_keys(Keys.ENTER)
    sleep(3)


@when(u'User click on approve button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'approveBtn')))
    driver.find_element_by_id('approveBtn').send_keys(Keys.ENTER)
    sleep(3)

@when(u'User click on Get Employee Info Btn')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'getEmpInfo')))
    driver.find_element_by_id('getEmpInfo').send_keys(Keys.ENTER)
    sleep(3)

@then(u'The employee is successfully approved.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logout')))
    driver.find_element_by_id('logout').click()
    sleep(3)

# Rejection #####################################################################
@given(u'The User is on the Management Page')
def step_impl(context):
    driver: WebDriver = context.driver
    driver.get("file:///Users/serignesamb/Desktop/CLIENTSIDE/AJAX/ProjectOne/management.html")
    sleep(3)

@when(u'User puts an employee id')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'employeeId')))
    driver.find_element_by_id('employeeId').send_keys("80")
    sleep(3)

@when(u'User presses on Get Employee Info button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'getEmpInfo')))
    driver.find_element_by_id('getEmpInfo').send_keys(Keys.ENTER)
    sleep(3)

@when(u'User clicks on reject button')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'rejectBtn')))
    driver.find_element_by_id('rejectBtn').send_keys(Keys.ENTER)
    sleep(3)


@when(u'User presses on Get Employee Info Btn')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'getEmpInfo')))
    driver.find_element_by_id('getEmpInfo').send_keys(Keys.ENTER)
    sleep(3)


@then(u'The employee is successfully rejected.')
def step_impl(context):
    driver: WebDriver = context.driver
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'logout')))
    driver.find_element_by_id('logout').click()
    sleep(3)
