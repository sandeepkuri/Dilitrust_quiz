import pytest
import time
from pytest_bdd import scenario, when, given
from locators.page_elements import Elements
from selenium.common.exceptions import StaleElementReferenceException
import robot


@scenario('../features/google_drive.feature', 'uploading file')
def test_uploading_file():
    pass

# Login with your google account


@given("User is already logged in")
def google_login(driver):
    driver.find_element_by_xpath(Elements.google_elements['log_in']).click()
    driver.find_element_by_xpath(Elements.google_elements['email_address']).send_keys("dili.sandeep@gmail.com")
    next_button = driver.find_element_by_xpath(Elements.google_elements['b_next'])
    next_button.click()
    driver.find_element_by_xpath(Elements.google_elements['password']).send_keys("dilitrust")
    try:
        next_button.click()
    except StaleElementReferenceException as Exception:
        print(Exception)
        driver.find_element_by_xpath(Elements.google_elements['b_next']).click()
    assert driver.find_element_by_xpath(Elements.google_elements['login_verify'])


@when('User is clicking on new')
def click_new(driver):
    driver.find_element_by_xpath(Elements.google_elements['b_new']).click()


@when('User is clicking on "file upload" and uploading the file')
def file_upload(driver):
    time.sleep(2)
    driver.find_element_by_xpath(Elements.google_elements['file_upload']).click()


@scenario('../features/google_drive.feature', 'dowloading file')
def test_downloading_file():
    pass


@when('user is clicking on file to download')
def file_download(driver):
    driver.find_element_by_xpath("//div[contains(text(),'Download all')]").click()

