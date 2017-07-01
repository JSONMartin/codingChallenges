from collections import Counter

class Solution(object):
    # O(n) solution with O(1) space
    def findDuplicates(self, nums):
        res = []
        for x in nums:
            absX = abs(x)
            if nums[absX-1] < 0:
                res.append(absX)
            else:
                nums[absX-1] *= -1
        return res
        
    # O(n) solution, but O(n) space
    def findDuplicatesO_N_space(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        results = []

        for c in counter:
            if counter[c] > 1:
                results.append(c)
        
        return results



nums = [4,3,2,7,8,2,3,1]
res = Solution().findDuplicates(nums)
print(res)