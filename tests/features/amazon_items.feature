# Created by sandeepkuri at 2020-01-18

Feature: Adding items to shopping cart
  As an Amazon user,
  I want to search items,
  So that I can Add them to my shopping cart.

  Scenario: Searching item
    Given User is at Amazon Home page
    When User is searching for "Samsung TV"
    And User is clicking on search icon
    Then User is presented with related results

  Scenario: Adding "Samsung tv" to the Cart
    Given User is at Selected Item page
    And There are no Item in the Cart
    When User is clicking on "Add to cart"
    Then User can see Item added to the cart

    # Enter steps here