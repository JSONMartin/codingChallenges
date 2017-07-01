from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for c in counter:
            if counter[c] == 1: return c
            
    def singleNumberWithCounter(self, nums):
        counter = Counter(nums)

        for c in counter:
            if counter[c] == 1: return c


### TEST ###
res = Solution().singleNumber([3, 2, 4, 3, 2])
print(res)