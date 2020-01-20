# Created by sandeepkuri at 2020-01-19

Feature: search flight
  As a User, I want to search flight for montreal to paris,
  So that I can fly there.

  Background:
    Given User is on Aircanada page
    And User select english language

  Scenario: flight search
    When user is entering Montreal for from Location
    And user is selecting Montreal
    And user is entering Paris for to location
    And user is selecting CDG
    And User is selecting dates
    And User is selecting the departing flights
    And User is selecting the returning flights
    And User is logging as a Guest
    Then User is able to input their information