# https://github.com/btjuhasz/lab11-bj
# Partner 1 Benjamin Juhasz
# Partner 2 Benjamin Juhasz (Working individually)

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):

    # Partner 1

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-10, 2), -5)
        self.assertEqual(div(5, 2), 2.5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(0, 4), 4)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(0), 0)
        with self.assertRaises(ValueError):
            square_root(-1)


if __name__ == "__main__":
    unittest.main()