import unittest
from enemy import Enemy


class TestEnemy(unittest.TestCase):
    def setUp(self) -> None:
        self.e1 = Enemy(1, 800, 770)

    def tearDown(self) -> None:
        print("tearDown\n")

    def test_enemy_speed(self):
        self.assertEqual(self.e1.enemy_level(10), 4)
        self.assertEqual(self.e1.enemy_level(30), 6)
        self.assertEqual(self.e1.enemy_level(50), 8)
        self.assertEqual(self.e1.enemy_level(70), 10)
        self.assertEqual(self.e1.enemy_level(100), 16)

    def test_add_enemy(self):
        self.e1.list = []
        while len(self.e1.list) < 6:
            self.e1.add_enemy()
        self.assertIsNotNone(self.e1.add_enemy())
        self.assertEqual(len(self.e1.add_enemy()), 6)

    def test_drop_enemy_score(self):
        self.e1.list = [[400, 400]]
        self.assertEqual(self.e1.drop_enemy(), 0)
        self.assertEqual(len(self.e1.list), 1)
        self.e1.list = [[400, 800]]
        self.assertEqual(self.e1.drop_enemy(), 1)
        self.assertEqual(len(self.e1.list), 0)
        # Once the enemy drops out of the height of the window,
        # add one point, and the position is removed from the list

    def test_collision(self):
        self.e1.list = [[350, 600]]
        self.assertTrue(self.e1.is_collision(400, 600, 32))
        self.e1.list = [[432, 600]]
        self.assertTrue(self.e1.is_collision(400, 600, 32))
        self.e1.list = [[400, 550]]
        self.assertTrue(self.e1.is_collision(400, 600, 32))
        self.e1.list = [[400, 632]]
        self.assertTrue(self.e1.is_collision(400, 600, 32))
        self.e1.list = [[400, 400]]
        self.assertFalse(self.e1.is_collision(400, 600, 32))
        self.e1.list = [[600, 600]]
        self.assertFalse(self.e1.is_collision(400, 600, 32))


if __name__ == '__main__':
    unittest.main()
