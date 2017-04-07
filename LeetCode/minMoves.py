# This was TLE
class Solution(object):
    def minMoves(self, nums):
        length, counter = len(nums), 0

        def isDiff(arr):
            first = arr[0]
            for el in arr:
                if el != first: return False
            return True


        #while len(set(nums)) > 1:
        while not isDiff(nums):
            counter += 1
            #print(nums)
            maxNum = max(nums)
            maxNumIdx = nums.index(maxNum)
            for i in range(length):
                if i != maxNumIdx: nums[i] += 1

        #print(counter)
        return counter



s = Solution()
#res = s.minMoves([1, 2, 3])
res = s.minMoves([1, 214744888])
print("Res:%d" % res)
