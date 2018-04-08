"""
Given array of integers, find the maximal possible sum of some of its k consecutive elements.

Example

For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
arrayMaxConsecutiveSum(inputArray, k) = 8.
All possible sums of 2 consecutive elements are:

2 + 3 = 5;
3 + 5 = 8;
5 + 1 = 6;
1 + 6 = 7.
Thus, the answer is 8.
"""


# Sliding Window solution, avoids summing subarrays to reduce complexity from O(n^2) to O(n)
def arrayMaxConsecutiveSum(inputArray, k):
    total = maxSoFar = sum(inputArray[:k])

    for i in range(1, len(inputArray) - k + 1):
        total = total - inputArray[i - 1] + inputArray[i + k - 1]
        maxSoFar = max(total, maxSoFar)

    return maxSoFar

# Works, but TLE for VERY large inputs - O(n^2)


def arrayMaxConsecutiveSumTLE(inputArray, k):
    maxSoFar = float('-inf')

    for i in range(len(inputArray) - k + 1):
        subArr = inputArray[i:i + k]
        print(subArr)
        maxSoFar = max(maxSoFar, sum(subArr))

    return maxSoFar


""" TESTS """
arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 3)
