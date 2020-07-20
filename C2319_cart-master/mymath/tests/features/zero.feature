Feature: User can login

  Scenario: User can log in
    When I go to the "home" URL
    Then I see "Login"

  Scenario: User can log in
    Given a user exists with username "try" and password "admin12345678"
    And I go to the "Login" URL
    and I fill in "Username" with "try"
    and I fill in "Password" with "admin12345678"
    and I press "Login"
    Then I should see "Hello try and welcome to College Market!"
