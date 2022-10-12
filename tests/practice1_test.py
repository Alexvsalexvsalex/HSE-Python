import unittest
from hse_python.practice_1 import *
from hse_python.utils.errors import IllegalArgumentError


class HelloworldTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(helloworld(0), [])
        self.assertEqual(helloworld(16), [
            "1", "2", "hello", "4", "world", "hello", "7", "8", "hello", "world",
            "11", "hello", "13", "14", "helloworld", "16"])


class OnesTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(ones([1, 1, 0, 1, 1, 1]), 3)
        self.assertEqual(ones([0]), 0)

    def test_empty_array(self):
        self.assertEqual(ones([]), 0)


class SumRangesTestCase(unittest.TestCase):
    def test_correctness(self):
        self.assertEqual(sum_ranges([0, 1, 2, 5, 8]), ["0->2", "5", "8"])
        self.assertEqual(sum_ranges([0, 1, 2, 4, 5, 7]), ["0->2", "4->5", "7"])
        self.assertEqual(sum_ranges([0, 1, 2, 3, 4, 5, 6, 7, 8]), ["0->8"])
        self.assertEqual(sum_ranges([0]), ["0"])
        self.assertEqual(sum_ranges([0, 2, 4, 6, 8]), ["0", "2", "4", "6", "8"])

    def test_incorrect_input(self):
        self.assertRaises(IllegalArgumentError, sum_ranges, [0, 3, 2])

    def test_empty_array(self):
        self.assertEqual(sum_ranges([]), [])


if __name__ == '__main__':
    unittest.main()
