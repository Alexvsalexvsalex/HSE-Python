import math
import unittest

from hse_python.practice_11 import *


class ComplexNumberTestCase(unittest.TestCase):
    number1 = ComplexNumber(1, 1)
    number2 = ComplexNumber(2, 2)
    number3 = ComplexNumber(-1, 0)

    def test_add(self):
        self.assertEqual(ComplexNumberTestCase.number1 + ComplexNumberTestCase.number2, ComplexNumber(3, 3))
        self.assertEqual(ComplexNumberTestCase.number2 + ComplexNumberTestCase.number3, ComplexNumber(1, 2))
        self.assertEqual(ComplexNumberTestCase.number1 +
                         ComplexNumberTestCase.number2 +
                         ComplexNumberTestCase.number3, ComplexNumber(2, 3))

    def test_sub(self):
        self.assertEqual(ComplexNumberTestCase.number1 - ComplexNumberTestCase.number2, ComplexNumber(-1, -1))
        self.assertEqual(ComplexNumberTestCase.number2 - ComplexNumberTestCase.number3, ComplexNumber(3, 2))
        self.assertEqual(ComplexNumberTestCase.number1 -
                         ComplexNumberTestCase.number2 -
                         ComplexNumberTestCase.number3, ComplexNumber(0, -1))

    def test_mul(self):
        self.assertEqual(ComplexNumberTestCase.number1 * ComplexNumberTestCase.number2, ComplexNumber(0, 4))
        self.assertEqual(ComplexNumberTestCase.number2 * ComplexNumberTestCase.number3, ComplexNumber(-2, -2))
        self.assertEqual(ComplexNumberTestCase.number1 *
                         ComplexNumberTestCase.number2 *
                         ComplexNumberTestCase.number3, ComplexNumber(0, -4))

    def test_abs(self):
        self.assertEqual(abs(ComplexNumberTestCase.number1), math.sqrt(2))
        self.assertEqual(abs(ComplexNumberTestCase.number2), math.sqrt(8))
        self.assertEqual(abs(ComplexNumberTestCase.number3), 1)


if __name__ == '__main__':
    unittest.main()
