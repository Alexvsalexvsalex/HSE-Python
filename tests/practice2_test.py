import unittest
from hse_python.practice_2 import *
from hse_python.utils.errors import IllegalArgumentError


class DiagonalSumTestCase(unittest.TestCase):
    def test_matrix_with_odd_size(self):
        self.assertEqual(diagonal_sum([[1]]), 1)
        self.assertEqual(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)

    def test_matrix_with_even_size(self):
        self.assertEqual(diagonal_sum([[1, 2], [3, 4]]), 10)

    def test_empty_matrix(self):
        self.assertEqual(diagonal_sum([]), 0)

    def test_incorrect_matrix(self):
        self.assertRaises(IllegalArgumentError, diagonal_sum, [[]])
        self.assertRaises(IllegalArgumentError, diagonal_sum, [[1], [2, 3]])
        self.assertRaises(IllegalArgumentError, diagonal_sum, [[1, 2, 3], [4, 5, 6]])


class MergeTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(merge([1, 2, 3], [0, 2, 5]), [0, 1, 2, 2, 3, 5])
        self.assertEqual(merge([-4, 7], [1, 1, 1]), [-4, 1, 1, 1, 7])

    def test_incorrect_input(self):
        self.assertRaises(IllegalArgumentError, merge, [1, 0], [2, 3])

    def test_empty_array(self):
        self.assertEqual(merge([], [0, 2, 5]), [0, 2, 5])
        self.assertEqual(merge([], []), [])


class SquaresTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(squares([-30, -10, -2, 0, 1, 5, 20]), [0, 1, 4, 25, 100, 400, 900])
        self.assertEqual(squares([-4, 4]), [16, 16])

    def test_incorrect_input(self):
        self.assertRaises(IllegalArgumentError, squares, [-2, 1, -1, 0])
        self.assertRaises(IllegalArgumentError, squares, [-1, 0, -2])

    def test_empty_array(self):
        self.assertEqual(squares([]), [])


class CompressTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(compress(["a", "b", "b", "c", "c", "c"]), "ab2c3")
        self.assertEqual(compress(["d", "a", "b", "c"]), "dabc")
        self.assertEqual(compress(["c", "c", "c"]), "c3")

    def test_incorrect_input(self):
        self.assertRaises(IllegalArgumentError, compress, ["0", "ab", "h"])

    def test_empty_array(self):
        self.assertEqual(compress([]), "")


if __name__ == '__main__':
    unittest.main()
