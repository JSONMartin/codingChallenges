# https://leetcode.com/problems/burst-balloons/
# Difficulty: Hard

"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
(1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
(2) 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Given [3, 1, 5, 8]

Return 167

    nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
   coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
"""
class Solution(object):
    def maxCoins(self, nums):
        try:
            if not nums or len(nums) <= 0: return 0
            elif len(nums) == 1: return nums[0]
            elif len(nums) == 2: return (min(nums) * max(nums)) + (max(nums))

            total, cur_max, cur_min, max_idx, min_idx = 0, float('-inf'), float('inf'), -1, -1

            while len(nums) > 2:
                min_val = float('inf')

                for i in range(1, len(nums) - 1):
                    cur_num = nums[i]
                    if nums[i] < min_val:
                        min_val = nums[i]
                        min_idx = i

                total += nums[min_idx - 1] * min_val * nums[min_idx + 1]
                nums.pop(min_idx)

            return total + (min(nums) * max(nums)) + (max(nums))
        except:
            return 0


        # while len(nums) > 0:
        #     n_list = [1] + nums + [1]
        #     for n in range(1, len(n_list) - 1):
        #         n_calc = n_list[n - 1] * n_list[n] * n_list[n + 1]
        #         if n_calc > cur_max:
        #             cur_max = n_calc
        #             max_idx = n
        #         if n_calc < cur_min:
        #             cur_min = n_calc
        #             min_idx = n
        #
        #     total += cur_max
        #     nums.pop(max_idx - 1)

        return total





        print(cur_max)
        print(cur_min)





### TESTS
nums = [3, 1, 5, 8]
s = Solution()
res = s.maxCoins(nums)

print(res)