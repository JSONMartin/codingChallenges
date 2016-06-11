class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if not needle or not haystack:
            return -1
        for i in range(len(haystack)):
            if i >= len(haystack) - len(needle) + 1: break
            elif haystack[i:len(needle) + i] == needle: return i
        return -1



"""TESTS"""

s = Solution()
s1 = "Hello my name is"
s2 = "name"

result = s.strStr(s1, s2)
print(result)
