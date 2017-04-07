"""
Given a string and an integer k, you need to reverse the first k characters for
every 2k characters counting from the start of the string. If there are less than
k characters left, reverse all of them. If there are less than 2k but greater than
or equal to k characters, then reverse the first k characters and left the other as original.
"""
class Solution(object):
    def reverseStr(self, s, k):
        result = ""

        for i in range(0, len(s), k * 2):
            subSection = s[i:i+(k*2)]            
            left, right = subSection[:k], subSection[k:]
            result += left[::-1] + right

        return result


# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"

s, k = "abcdefg", 2
Solution().reverseStr(s, k)
