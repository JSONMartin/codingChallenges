"""
Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        def binarySearch(low, high):
            mid = (low + high) // 2
            # Base Case
            if low == high:
                if nums[mid] == target: return mid
                else: return -1
            if low >= high:
                return -1
            
            # Binary searching
            if nums[mid] == target: return mid
            elif nums[mid] > target: return binarySearch(low, mid - 1)
            elif nums[mid] < target: return binarySearch(mid + 1, high)

        try:
            location = binarySearch(0, len(nums) - 1)
            if location == -1: raise Exception
        except:
            return [-1, -1]
        
        left, right = location, location

        # Find left bound
        while True:
            if left > 0 and nums[left - 1] == target:
                left -= 1
            else:
                break
        
        # Find right bound
        while True:
            if right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            else:
                break
        
        return [left, right]


### TESTING ###
result = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
#result = Solution().searchRange([1], 0)
#result = Solution().searchRange([1], 1)
#result = Solution().searchRange([2, 2], 3)
print(result)