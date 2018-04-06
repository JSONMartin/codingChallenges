"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

For product = 12, the output should be
digitsProduct(product) = 26;
For product = 19, the output should be
digitsProduct(product) = -1.
"""
from functools import reduce


def digitsProduct(product):
    digitToTry = 1

    while True:
        digitStr = str(digitToTry)
        digitTotal = 0

        if digitToTry > 100000:  # Set a breakpoint for numbers not to check above
            return -1
        if len(digitStr) == 1 and digitToTry == product:
            return digitToTry
        elif len(digitStr) > 1:
            digitTotal = reduce(lambda x, y: x * y, map(lambda string: int(string), digitStr), 1)
            if digitTotal == product:
                return digitToTry

        digitToTry += 1


""" TESTS """
digitsProduct(12)
