__author__ = 'root'

import unittest
from score.team import Team


class TeamTestCase(unittest.TestCase):
    def test_team_can_be_created(self):
        team = Team("Gilas", 0)
        self.assertEqual(team.team_name, "Gilas")
        self.assertEqual(team.score, 0)


if __name__ == '__main__':
    unittest.main()
