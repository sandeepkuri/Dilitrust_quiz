import pytest
import time
from pytest_bdd import scenario, when
from locators.page_elements import Elements
import robot


@scenario('../features/google_drive.feature', 'uploading file')
def test_uploading_file():
    pass


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
    driver.find_element_by_xpath("//div[contains(text(),'Screen Shot 2020-01-17 at 7.07.25 AM.png')]").click()
    driver.find_element_by_xpath("(//div[@data-tooltip='More actions'])[1]").click()
