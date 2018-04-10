from fractions import gcd
from functools import reduce


def leastCommonDenominator(denominators):
    return reduce(lambda x, y: (x * y) // gcd(x, y), denominators)
