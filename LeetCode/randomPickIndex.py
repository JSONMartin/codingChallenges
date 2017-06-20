"""
# https://leetcode.com/problems/random-pick-index/#/description
"""
import random

class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        indexes = []

        # Slower, but more elegant
        for idx, num in enumerate(self.nums):
            if num == target:
                indexes.append(idx)
        
        # for i in xrange(len(self.nums)):
        #     if self.nums[i] == target:
        #         indexes.append(i)

        randIdx = random.randint(0, len(indexes) - 1)
        result = indexes[randIdx]
        return result


# Your Solution object will be instantiated and called as such:
obj = Solution(nums)
#param_1 = obj.pick(target)