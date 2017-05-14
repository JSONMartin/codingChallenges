"""
https://leetcode.com/problems/maximum-subarray/#/description

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""
class Solution(object):
    def maxSubArray(self, nums):
        maxNums = [nums[0]]

        for i in range(1, len(nums)):
            total = maxNums[i - 1] + nums[i]
            maxNums += [max(total, nums[i])]
        
        return max(maxNums)
        
    def maxSubArraySaveSubArray(self, nums):
        maxNums = [(nums[0], [nums[0]])]

        for i in range(1, len(nums)):
            total = maxNums[i - 1][0] + nums[i]

            if total > nums[i]:
                maxNums += [(total, (maxNums[i - 1][1] + [nums[i]]))]
            else:
                maxNums += [(nums[i], [nums[i]])]
        
        return sorted(maxNums, key=lambda x: x[0], reverse=True)[0]
        
### TESTS ###

res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(res)

