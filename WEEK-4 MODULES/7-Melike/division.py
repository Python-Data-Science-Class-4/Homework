
import math


def division(a, b):
    try:
        print(ceil(a / b))
    except ZeroDivisionError:
        print("The divisor number in division cannot be 0")