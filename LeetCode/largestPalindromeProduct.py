"""
# https://leetcode.com/problems/largest-palindrome-product/#/description

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""
class Solution(object):
    def largestPalindrome(self, n):
        #matches = []
        if n == 1: return 9
        max_n = float('-inf')
        startNum, stopNum = int("9" * n), int("1" + "0" * (n-1))
        #print(startNum, stopNum)
        for n1 in range(startNum, stopNum, -1):
            for n2 in range(startNum, stopNum, -1):
                
                numberStr = str(n1 * n2)
                #print(n1, n2, int(numberStr) % 1337)
                if numberStr == numberStr[::-1]:
                    #print("MATCH FOUND!:", numberStr)
                    #return int(numberStr) % 1337
                    n = int(numberStr)
                    max_n = max(n, max_n)
                    #matches.append((n, n%1337))
        return max_n % 1337
        #print(max_n, max_n % 1337)

res = Solution().largestPalindrome(4)
print(res)