import unittest
from sort import insertion_sort

class TestInsertionSort(unittest.TestCase):

    def test_sorted_list(self):
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(insertion_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])

    def test_single_element_list(self):
        self.assertEqual(insertion_sort([1]), [1])

    def test_empty_list(self):
        self.assertEqual(insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main()