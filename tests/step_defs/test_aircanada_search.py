from pytest_bdd import scenario, when, then
from locators.page_elements import Elements
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


@scenario('../features/aircanada_search.feature', 'flight search')
def test_flight_search():
    pass

    # Selecting Montreal as From


@when("user is entering Montreal for from Location")
def from_location(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['from_']).clear()
    driver.find_element_by_xpath(Elements.aircanda_elements['from_']).send_keys(Elements.FROM)


@when('user is selecting Montreal')
def select_montreal(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['from_montreal']).click()

    # Selecting Paris as To


@when('user is entering Paris for to location')
def to_location(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['to_']).send_keys("paris")


@when('user is selecting CDG')
def select_cdg(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['to_paris']).click()

    # Selecting Dates


@when('User is selecting dates')
def select_dates(driver):
    driver.find_element_by_xpath(Elements.aircanda_elements['select_date']).click()
    time.sleep(2)
    driver.find_element_by_xpath(Elements.aircanda_elements['select_02']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['select_20']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['select_button']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['no_flexible']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['find_button']).click()


@when('User is selecting the departing flights')
def select_departing_flight(driver):

    # waiting for page to load

    try:
        element_present = EC.presence_of_element_located((By.ID, 'boundTitleGridContainer'))
        WebDriverWait(driver, Elements.timeout).until(element_present)
        print("Departing flight page loaded successfully")
    except TimeoutException:
        print("Timed out waiting for Departing flight page to load")

    # Selecting Departure flight

    driver.implicitly_wait(2)
    driver.find_element_by_xpath(Elements.aircanda_elements['Select_D_flight']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['Select_cl_V']).click()


@when('User is selecting the returning flights')
def select_returning_flight(driver):

    # Waiting for page to load

    try:
        element_present = EC.presence_of_element_located((By.XPATH, Elements.aircanda_elements['return_flight_page_V']))
        WebDriverWait(driver, Elements.timeout).until(element_present)
        print("Returning flight page loaded successfully")
    except TimeoutException:
        print("Timed out waiting for Returning flight page to load")

    # Selecting return flights

    driver.find_element_by_xpath(Elements.aircanda_elements['Select_R_flight']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['Select_al_V']).click()


@when('User is logging as a Guest')
def guest_login(driver):

    # Waiting for page to load

    try:
        element_present = EC.presence_of_element_located((By.XPATH, Elements.aircanda_elements['continue_after_selection']))
        WebDriverWait(driver, Elements.timeout).until(element_present)
        print("Page loaded")
    except TimeoutException:
        print("Timed out waiting for page to load")

    # Booking as a Guest

    driver.find_element_by_xpath(Elements.aircanda_elements['continue_after_selection']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['book_as_guest']).click()


@then('User is able to input their information')
def guest_information(driver):

    # Waiting for page to load

    try:
        element_present = EC.presence_of_element_located((By.XPATH, Elements.aircanda_elements['first_name']))
        WebDriverWait(driver, Elements.timeout).until(element_present)
        print("User information page loaded successfully")
    except TimeoutException:
        print("Timed out waiting for P page to load")

    # Entering user information

    driver.find_element_by_xpath(Elements.aircanda_elements['first_name']).send_keys(Elements.F_NAME)
    driver.find_element_by_xpath(Elements.aircanda_elements['last_name']).send_keys(Elements.L_NAME)
    driver.find_element_by_xpath(Elements.aircanda_elements['DOB']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['DOB_02']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['MOB']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['MOB_FEB']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['YOB']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['YOB_1997']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['gender']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['gender_male']).click()
    driver.find_element_by_xpath(Elements.aircanda_elements['C_phone']).send_keys(Elements.P_NUMBER)
    driver.find_element_by_xpath(Elements.aircanda_elements['c_email']).send_keys(Elements.EMAIL_ADDRESS)
    driver.find_element_by_xpath(Elements.aircanda_elements['Final']).click()
