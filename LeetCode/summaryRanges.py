"""
# https://leetcode.com/problems/summary-ranges/#/description

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
"""
class Solution(object):
    def summaryRanges(self, nums):
        try:
            ranges = []
            curRange = []
            for n in nums:
                if len(curRange) == 0:
                    curRange.append(n)
                    continue
                if n == curRange[-1] + 1:
                    curRange.append(n)
                else:
                    ranges.append(curRange[:])
                    curRange = [n]
            
            ranges.append(curRange)
            rangesStr = ["{0}->{1}".format(r[0], r[-1]) if len(r) > 1 else str(r[0]) for r in ranges]
            return rangesStr
        except:
            return []

        # try:
        #     if len(nums) == 1: return [str(nums[0])]
        #     ranges = []
        #     start, end = nums[0], None
            
        #     for i in range(1, len(nums)):
        #         if nums[i] != nums[i - 1] + 1:
        #             end = nums[i - 1]
        #             if start == end: ranges.append(str(start))
        #             else: ranges.append("{0}->{1}".format(start, end))
        #             start = nums[i]
            
        #     if start == nums[0]:
        #         ranges.append("{0}->{1}".format(nums[0], nums[-1]))
        #     elif start and end == None:
        #         ranges.append(str(start))
        #     else:
        #         ranges.append("{0}->{1}".format(start, end))
            

        #     print(ranges)
        #     return ranges
        # except:
        #     return []


#test = [0,1,2,4,5,7]
#test = [0, 1]
test = [0, 8, 9]
Solution().summaryRanges(test)