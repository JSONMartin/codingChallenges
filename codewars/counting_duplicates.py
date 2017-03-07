# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1/solutions/python

import collections

def duplicate_count(text):
    print(text)
    c = collections.Counter(text.upper())
    results = []

    for key in c:
        if c[key] > 1: results.append(key)

    return len(results)