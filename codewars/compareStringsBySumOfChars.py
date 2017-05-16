# https://www.codewars.com/kata/576bb3c4b1abc497ec000065/solutions/python

import re

def compare(s1,s2):
    if not s1 or re.search(r'[^a-zA-Z]', s1): s1 = ''
    if not s2 or re.search(r'[^a-zA-Z]', s2): s2 = ''
    s1 = list(map(ord, s1.upper())); s2 = list(map(ord, s2.upper()))
    return sum(s1) == sum(s2)

### TESTS ###
res = compare("asdf", "fdSa1")
print(res)