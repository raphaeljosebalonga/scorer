__author__ = 'papershoppe'

from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from scorer_app import APP, SCORER
from score.team import Team

@step(u'Given I have 2 teams "([^"]*)" with scores "([^"]*)"')
def given_i_have_2_teams_group1_with_scores_group2(step, team_name, score):
    team = Team(team_name, score)
    SCORER.add_team(team)

@step(u'When I visit the homepage')
def when_i_visit_the_homepage(step):
    world.browser = TestApp(APP)
    world.response = world.browser.get('http://localhost:5000/')
    assert_equal(world.response.status_code, 200)

@step(u'Then I see the score "([^"]*)"')
def then_i_see_the_score_group1(step, score):
    assert_in("Score: {}".format(score), world.form_response.text)