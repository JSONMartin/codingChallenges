class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        clean_str = ''.join(ch.lower() for ch in A if ch.isalnum() and ch != ' ')
        print(clean_str)
        return clean_str == clean_str[::-1]



"""TESTS"""

s = Solution()

#res = s.isPalindrome("A man, a plan, a canal: Panama")
res = s.isPalindrome("1a2")
#res = s.isPalindrome("racecar s")
print(res)