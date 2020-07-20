import unittest
from score import Score


class TestScore(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Score(1, 30)
        self.s2 = Score(1, 40)

    def tearDown(self) -> None:
        print("tearDown\n")

    def test_highest_score_storing(self):
        with open("bestscore.txt", "w") as f:
            f.write(str(0))
        self.assertEqual(self.s1.store_highest_score(), 30)
        self.assertEqual(self.s2.store_highest_score(), 40)
        '''
        Write 0 in the file as the original highest score
        If the current score is larger than 0 (test 30, 40),
        the file will be overwritten with the current score.
        '''


if __name__ == '__main__':
    unittest.main()