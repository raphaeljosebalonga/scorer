Feature: Scorer Web Application that retrieves and update team scores
As a scorer I want to be able to view the teams' scores
and update the scores


Scenario Outline: View teams' scores
    Given I have 2 teams "Gilas" with scores "99"
    When I visit the homepage
    Then I see the score "99"