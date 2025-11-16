
# https://github.com/Lethanial-Leveille/lab11-LL-DW.git
# Partner 1: Lethanial Leveille
# Partner 2: Dylan Wells

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b



def logarithm(a, b):
    # log base a of b
    if a <= 0 or a == 1:
        raise ValueError("Invalid base for logarithm")
    if b <= 0:
        raise ValueError("Invalid argument for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Invalid arguments")
    return math.log(b, a)

def exp(a, b):
    return a ** b