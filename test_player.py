import unittest
from player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.p1 = Player(1, 32, 800, 770)

    def tearDown(self) -> None:
        print("tearDown\n")

    def test_player_movement(self):
        self.assertEqual(self.p1.player_movement(0), 400)
        self.assertEqual(self.p1.player_movement(800), 800-32)
        self.assertEqual(self.p1.player_movement(-800), 0)
        '''
        p1 cannot display out of the window boundary.
        Once its x is not in the range of window width or its y is out of range of window height.
        The program will correct it automatically.
        
        '''


if __name__ == '__main__':
    unittest.main()








