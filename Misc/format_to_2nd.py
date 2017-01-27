# https://www.codewars.com/kata/format-to-the-2nd/train/python

"""
Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. No leading zeroes shall be added to the largest integer.

For example, given 1, 23, 2, 17, 102, the following string should be printed out:

001
023
002
017
102
Write a function print_nums(n1, n2, n3, ...) that takes a variable number of arguments and returns the string to be printed out.
"""

def print_nums(*args):
    try:
        max_length = len(str(max(args)))
        return "\n".join(['0' * (max_length - len(n)) + n for n in map(str,args)])
    except:
        return ''

### TESTS
res = print_nums(1, 12, 34)
print(res)

