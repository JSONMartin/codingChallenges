# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

from collections import Counter

def find_it(seq):
    counter = Counter(seq)

    for c in counter:
        if counter[c] % 2 == 1:
            return c

    return None
