import unittest
from hanoi import solve_hanoi

class TestHanoi(unittest.TestCase):

    def setUp(self):
        self.moves = []

    def test_hanoi_1_disk(self):
        solve_hanoi(1, 'A', 'C', 'B', self.moves)
        self.assertEqual(self.moves, [('A', 'C')])

    def test_hanoi_2_disks(self):
        solve_hanoi(2, 'A', 'C', 'B', self.moves)
        expected_moves = [('A', 'B'), ('A', 'C'), ('B', 'C')]
        self.assertEqual(self.moves, expected_moves)

    def test_hanoi_3_disks(self):
        solve_hanoi(3, 'A', 'C', 'B', self.moves)
        expected_moves = [
            ('A', 'C'), ('A', 'B'), ('C', 'B'),
            ('A', 'C'), ('B', 'A'), ('B', 'C'), ('A', 'C')
        ]
        self.assertEqual(self.moves, expected_moves)

if __name__ == '__main__':
    unittest.main()