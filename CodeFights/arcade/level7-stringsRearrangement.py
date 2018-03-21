"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.

Example

For inputArray = ["aba", "bbb", "bab"], the output should be
stringsRearrangement(inputArray) = false;

All rearrangements don't satisfy the description condition.

For inputArray = ["ab", "bb", "aa"], the output should be
stringsRearrangement(inputArray) = true.

Strings can be rearranged in the following way: "aa", "ab", "bb".
Input/Output
"""
from itertools import permutations


def memoize(fn):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = fn(*args)
            return cache[args]

    return wrapper


@memoize
def wordDifferentByOneChar(word1, word2):
    differences = 0

    for idx in range(len(word1)):
        if word1[idx] != word2[idx]:
            differences += 1
        if differences > 1:
            return False

    return differences == 1


def stringsRearrangement(inputArray):
    allPossible = tuple(permutations(inputArray))
    for possible in allPossible:
        foundPossibility = True

        for idx in range(len(possible) - 1):
            word1, word2 = possible[idx], possible[idx + 1]

            if wordDifferentByOneChar(word1, word2) is False:
                foundPossibility = False
                break

        if foundPossibility:
            return True

    return False


""" TESTS """

# res = stringsRearrangement(["abc", "abx", "axx", "abc"])
# res = stringsRearrangement(["aba", "bbb", "bab"])
res = stringsRearrangement(["abc",
                            "bef",
                            "bcc",
                            "bec",
                            "bbc",
                            "bdc"])
# res = stringsRearrangement(["ab", "bb", "aa"])
print(res)
