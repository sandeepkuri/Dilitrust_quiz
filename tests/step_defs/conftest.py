import pytest
from selenium import webdriver
from pytest_bdd import given
from locators.page_elements import Elements
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options


# Fixtures

# Setting up the chrome borwser

@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--temp-basedir")
    driver = webdriver.Chrome(executable_path="/Users/sandeepkuri/Dilitrust/drivers/chromedriver", chrome_options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()


# Shared Given Steps(Background steps)


# Background steps for Google Drive


@given('User is on google drive page')
def google_drive_page(driver):
    driver.get(Elements.GOOGLE_DRIVE_PAGE)


# Background steps for AirCanada


@given("User is on Aircanada page")
def aircanada_page(driver):
    driver.get(Elements.AIRCANADA_PAGE)


@given("User select english language")
def select_language(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['select_english']).click()

