class Solution(object):
    def isPowerOfFour(self, num):
        i = 0

        while i < (num / 4):
            if 4**i == num: return True
            else: i += 1

        return False

### TESTS
s = Solution()

res = s.isPowerOfFour(253)
print(res)
