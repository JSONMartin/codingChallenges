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


def stringsRearrangement(inputArray):
    allPossible = tuple(permutations(inputArray))
    # print(allPossible)
    memo = {}

    def checkPossibility(current, remaining=[]):
        print(current, remaining)
        if len(remaining) == 0:
            return True
        return checkPossibility(current + (remaining[0], ), remaining[1:])

    checkPossibility((), tuple(inputArray))


def stringsRearrangementTLE(inputArray):
    allPossible = list(permutations(inputArray))
    maxDifference = float('-inf')

    maxDifferences = []

    memo = {}

    # Scan through each possibility, and check if each matching pair is only a character off
    for possibility in allPossible:
        total = 0
        differences = []
        # print(possibility)
        for idx in range(len(possibility) - 1):
            str1, str2 = possibility[idx], possibility[idx + 1]
            sortedStrs = sorted((str1, str2))
            KEY = list(sortedStrs)[0] + '-' + list(sorted(sortedStrs))[1]
            if KEY in memo:
                differences += [memo[KEY]]
                continue
            # print(KEY)
            totalDifferences = 0
            for charIdx in range(len(possibility[idx])):
                charA, charB = str1[charIdx], str2[charIdx]

                if totalDifferences > 1:
                    break
                if charA != charB:
                    totalDifferences += 1

            memo[KEY] = totalDifferences if totalDifferences > 0 else float('inf')

            differences += [memo[KEY]]
            # print(differences)

        maxDifferences += [max(differences)]

        if min(maxDifferences) <= 1:
            return True

    # print(maxDifferences)
    return False

# def stringsRearrangement(inputArray):
#     allPossible = list(permutations(inputArray))
#     maxDifference = float('-inf')

#     maxDifferences = []

#     # Scan through each possibility, and check if each matching pair is only a character off
#     for possibility in allPossible:
#         total = 0
#         differences = []
#         # print(possibility)
#         for idx in range(len(possibility) - 1):

#             totalDifferences = 0
#             for charIdx in range(len(possibility[idx])):
#                 charA, charB = possibility[idx][charIdx], possibility[idx + 1][charIdx]
#                 # print("Comparing these chars: %s | %s" % (charA, charB))

#                 if charA != charB:
#                     totalDifferences += 1

#             differences += [totalDifferences if totalDifferences > 0 else float('inf')]
#             # print(differences)

#         maxDifferences += [max(differences)]

#     # print(maxDifferences)
#     if min(maxDifferences) <= 1:
#         return True
#     return False


# res = stringsRearrangement(["abc", "abx", "axx", "abc"])
# res = stringsRearrangement(["aba", "bbb", "bab"])
res = stringsRearrangement(["ab", "bb", "aa"])
print(res)
