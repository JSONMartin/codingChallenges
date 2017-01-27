# https://www.codewars.com/kata/powers-of-2/train/python
"""
Write a function powersOfTwo which will return list of all powers of 2 from 0 to n (where n is an exponent).

E.g:

n = 0 -> 2^0 -> [1]

n = 1 -> 2^0, 2^1 -> [1,2]

n = 2 -> 2^0, 2^1, 2^2 -> [1,2,4]
"""

# Original, slower
powers_of_two_og = lambda n: [2**i for i in range(n + 1)]

# Improved binary shift version, faster
powers_of_two = lambda n: [1<<i for i in range(n + 1)]


"""
TESTS
"""
res = powers_of_two(4)
print(res)