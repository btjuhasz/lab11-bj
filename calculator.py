# https://github.com/btjuhasz/lab11-bj
# Partner 1 Benjamin Juhasz
# Partner 2 Benjamin Juhasz (Working individually)

import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid logarithm base or argument")
    return math.log(b, a)


def exp(a, b):
    return a ** b


def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)