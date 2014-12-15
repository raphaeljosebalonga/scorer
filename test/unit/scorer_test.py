__author__ = 'root'

import unittest
from score.scorer import Scorer
from score.team import Team


class ScorerTestCase(unittest.TestCase):
    def test_score_is_initially_zero(self):
        scorer = Scorer()
        self.assertEqual({}, scorer.teams)
        self.assertEqual(len(scorer.teams), 0)

    def test_add_team(self):
        scorer = Scorer()

        team_1 = Team("Alas", 0)
        team_2 = Team("Gilas", 0)

        scorer.add_team(team_1)
        scorer.add_team(team_2)

        self.assertEqual(len(scorer.teams), 2)

    def test_add_score(self):
        scorer = Scorer()

        team_1 = Team("samting", 0)

        scorer.add_team(team_1)

        scorer.add_score(team_1, 2)

if __name__ == '__main__':
    unittest.main()
