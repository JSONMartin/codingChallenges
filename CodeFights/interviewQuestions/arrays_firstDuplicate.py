"""
https://codefights.com/interview-practice/task/pMvymcahZ8dY4g75q/description


Note: Write a solution with O(n) time complexity and O(1) additional space complexity, since this is what you would be asked to do during a real interview.

Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

Example

For a = [2, 3, 3, 1, 5, 2], the output should be
firstDuplicate(a) = 3.

There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a smaller index than than second occurrence of 2 does, so the answer is 3.

For a = [2, 4, 3, 5, 1], the output should be
firstDuplicate(a) = -1.
"""


def firstDuplicate(a):
    for n in a:
        idx = abs(n) - 1
        a[idx] *= -1
        if a[idx] > 0: return abs(-idx - 1)

    return -1


"""
This solution is O(n) and O(1) space complexity.

It marks the indexes of the array multiplied by -1.

After multiplying by -1, the first positive result is the first duplicate index.
"""

""" TESTS """
res = firstDuplicate([2, 2])
print(res)
