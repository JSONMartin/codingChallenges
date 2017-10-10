"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        LENGTH = len(s)
        if LENGTH == 0: return 0
        dp = [0] * (LENGTH + 1)
        dp[0] = 1

        for i in range(1, len(s) + 1):
            singleDigit = s[i - 1]
            doubleDigit = s[i-2:i]
            
            if singleDigit != "0":
                dp[i] += dp[i - 1]
            if i > 1 and doubleDigit < "27" and doubleDigit > "09":
                dp[i] += dp[i - 2]

            # print(singleDigit, doubleDigit, dp)
        
        return dp[-1]


### TESTS

res = Solution().numDecodings("1212")
#res = Solution().numDecodings("230")
#res = Solution().numDecodings("12120")
#res = Solution().numDecodings("101")
#res = Solution().numDecodings("20")

print("Res:%d" % res)