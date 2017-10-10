"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray
of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

# Sliding Window Solution
class Solution(object):
    def minSubArrayLen(self, s, nums):
        start, end, curTotal, minimum = 0, 0, 0, float('inf')
        LENGTH = len(nums) - 1

        while start <= LENGTH:
            if curTotal >= s:
                minimum = min(end - start, minimum)
                curTotal -= nums[start]
                start += 1
            elif end <= LENGTH:
                curTotal += nums[end]
                end += 1
            else:
                curTotal -= nums[start]
                start += 1

        return minimum if minimum < float('inf') else 0

### TESTING ###

# Solution().minSubArrayLen(7, [2,3,1,2,4,3])
Solution().minSubArrayLen(11, [1, 2, 3, 4, 5])
