import math

class Solution(object):
    def convertToTitle(self, n):
        res = ""

        while n > 0:
            letter = (n - 1) % 26
            res += chr(65 + letter)
            n = (n - 1) // 26

        return res[::-1]


res = Solution().convertToTitle(28)
print(res)