__author__ = 'papershoppe'

""" Scorer Module """


class Scorer(object):
    """ Scorer Class """
    def __init__(self):
        self.teams = {}

    def add_team(self, team):
        """ Setter Method """
        self.teams[team.team_name] = team.score

    def get_team_score(self, team_name): # pragma: no cover
        """ Getter Method """
        return self.teams.get(team_name)

    def add_score(self, team, score_add):
        self.teams[team.team_name] = team.score + score_add