from pytest_bdd import scenario, given, when, then
from locators.page_elements import Elements

# This testing script verifying the working status of Aamazon search items and Adding item to the cart


@scenario('../features/amazon_items.feature', 'Searching item')
def test_search_item(driver):
    pass

# Going to Amazon Home page


@given("User is at Amazon Home page")
def amazon_home_page(driver):
    driver.get(Elements.AMAZON_HOME)

# Searching for item "Samsung TV"


@when('User is searching for "Samsung TV"')
def search_tv(driver):
    driver.find_element_by_xpath(Elements.amazon_element['search_imput']).send_keys(Elements.SEARCH_VALUE)


@when('User is clicking on search icon')
def search_icon(driver):
    driver.find_element_by_xpath(Elements.amazon_element['search_button']).click()


# Checking if it is loading the results


@then('User is presented with related results')
def search_results(driver):
    assert driver.find_element_by_xpath(Elements.amazon_element['search_results'])


# This part of the script Adding an Item to the Cart and confirming that

@scenario('../features/amazon_items.feature', 'Adding "Samsung tv" to the Cart')
def test_adding_item(driver):
    pass


# Going to selected item

@given('User is at Selected Item page')
def item_link(driver):
    driver.get(Elements.AMAZON_HOME + Elements.SAMSUNG_TV)


@given('There are no Item in the Cart')
def empty_cart(driver):
    assert driver.find_element_by_xpath(Elements.amazon_element['zero_item'])

# Adding Item to the cart


@when('User is clicking on "Add to cart"')
def add_to_cart(driver):
    driver.find_element_by_xpath(Elements.amazon_element['add_tv']).click()

# Verifying that the item is added to the cart


@then('User can see Item added to the cart')
def item_added(driver):
    assert driver.find_element_by_xpath(Elements.amazon_element['verify_item'])

