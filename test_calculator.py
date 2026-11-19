# https://github.com/btjuhasz/lab11-bj
# Partner 1 Benjamin Juhasz
# Partner 2 Benjamin Juhasz (Working individually)

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-10, 2), -5)
        self.assertAlmostEqual(div(5, 2), 2.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-5, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)

    #===============================================

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(5, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(1, 2), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(5, -2)


if __name__ == "__main__":
    unittest.main()