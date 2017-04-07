# https://leetcode.com/problems/valid-palindrome/#/description
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.
"""
import re

class Solution(object):
    def isPalindrome(self, s):
        stripped = re.sub(r"[^a-zA-Z0-9]", "", s.upper())
        length = len(stripped)

        for i in range(length / 2):
            if stripped[i] != stripped[length - 1 - i]: return False

        return True



res = Solution().isPalindrome("0P")
print(res)
