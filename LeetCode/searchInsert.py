class Solution(object):
    def searchInsert(self, nums, target):
        if target < nums[0]: return 0

        for i in xrange(len(nums)):
            if nums[i] == target: return i
            elif i + 1 >= len(nums): return len(nums)
            elif nums[i] < target < nums[i + 1]: return i + 1