# https://leetcode.com/problems/maximum-product-subarray/#/description

class Solution(object):
    # Dynamic Programming solution, beats 78.10% of Python submissions
    def maxProduct(self, nums):
        numsDPmax, numsDPmin = nums[:], nums[:]
        length = len(nums)

        for i in range(1, length):
            numsDPmax[i] = max(numsDPmax[i], numsDPmax[i] * numsDPmax[i - 1], numsDPmax[i] * numsDPmin[i - 1])
            numsDPmin[i] = min(numsDPmin[i], numsDPmin[i] * numsDPmin[i - 1], numsDPmin[i] * numsDPmax[i - 1])

        return max(numsDPmax)


    # TLE Solution
    def maxProductAllPossabilities(self, nums):
        length = len(nums)
        maximumVal, maximumArr = float('-inf'), []

        for i in range(length + 1):
            for j in range(i + 1, length + 1):
                subArr = nums[i:j]
                print(subArr)

                product = 1
                for n in subArr:
                    product *= n

                if product > maximumVal:
                    maximumVal = product; maximumArr = subArr[:]

        return maximumVal








###
#res = Solution().maxProduct([2, 3, -2, 4])
res = Solution().maxProduct([-2, 3, -4])
print(res)