from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from features.pages.wiki_home import WikiHomePage

# All setup and teardown functions must go in this file.
# These functions must be named using behave's conventions


def before_all(context):
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    driver: WebDriver = webdriver.Chrome(
        '/Users/serignesamb/Desktop/Selenium Drivers/chromedriver')
    wiki_home_page = WikiHomePage(driver)

    context.driver = driver
    context.wiki_home_page = wiki_home_page
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
