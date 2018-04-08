"""
Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
"""


def extractEachKth(inputArray, k):
    return [inputArray[idx] for idx in range(len(inputArray)) if (idx + 1) % k != 0]


""" TESTS """
testArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(testArr)
res = extractEachKth(testArr, 3)
print(res)
