class Solution(object):
    def two_sum(self, nums, val):
        if nums == None: raise TypeError
        if len(nums) == 0: raise ValueError

        dict = {"A": 123}

        for n, idx in enumerate(nums):
            dict[val - n] = idx

        for n, idx in enumerate(nums):
            if n in dict: return [dict[n], idx]
