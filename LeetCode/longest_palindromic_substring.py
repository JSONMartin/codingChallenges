class Solution:
    # @param A : string
    # @return a strings

    def longestPalindrome(self, string):
        max_length = 1

        start = 0
        length = len(string)

        low = 0
        high = 0

        for i in range(1, length):
            low = i - 1
            high = i

            # Finds evens
            while low >= 0 and high < length and string[low] == string[high]:
                print(max_length)
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

            # Find odds
            low = i - 1
            high = i + 1
            while low >= 0 and high < length and string[low] == string[high]:
                print(max_length)
                if high - low + 1 > max_length:
                    start = low
                    max_length = high - low + 1
                low -= 1
                high += 1

            # print("Longest str is:")
            # print(string[start:start + max_length])

        return string[start:start + max_length]


    # Brute Force solution
    def longestPalindromeOG(self, A):
        result = ""

        for i in range(len(A)):
            j = int(len(A))
            while j > i:
                cur_str = A[i:j]
                print(cur_str)
                print(reversed(cur_str))
                if cur_str == cur_str[::-1] and len(cur_str) > len(result):
                    result = cur_str
                j-=1

        return result

s = Solution()
"""
TESTS
"""
res = s.longestPalindrome("aaaabaaa")
#res = s.longestPalindrome("abb")
print("Result:", res)