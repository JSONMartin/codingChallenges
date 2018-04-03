"""
A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

Given a string, check whether it is beautiful.
"""
from collections import Counter


def isBeautifulString(inputString):
    letterCount = Counter(inputString)

    for letter in inputString:
        if letter != 'a' and letterCount[letter] > letterCount[chr(ord(letter) - 1)]:
            return False

    return True


""" TESTS """
# res = isBeautifulString("bbbaacdafe")  # ==> True
res = isBeautifulString('aabbb')  # ==> False

print("Result:", res)
