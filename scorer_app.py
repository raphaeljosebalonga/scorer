__author__ = 'papershoppe'

""" Scorer App Module """
from flask import Flask, render_template, request

from score.scorer import Scorer
from score.team import Team

APP = Flask(__name__)
SCORER = Scorer()

@APP.route('/')
def hello_world():
    team_name = request.args.get('team_name')
    score = SCORER.get_team_score(team_name)
    return render_template('index.html', score=score)

if __name__ == '__main__':
    team1 = Team('Gilas', 100)
    team2 = Team('Ahas', 99)
    SCORER.add_team(team1)
    SCORER.add_team(team2)
    APP.run(debug=True)