class Solution(object):
    def lengthOfLongestSubstring(self, s):
        LENGTH = len(s)
        longestSubstringSize, i, j = 0, 0, 0
        window = set()

        while i < LENGTH and j < LENGTH:
            if s[j] not in window:
                window.add(s[j])
                j += 1
                longestSubstringSize = max(j - i, longestSubstringSize)
            else:
                window.remove(s[i])
                i += 1
        
        return longestSubstringSize


    # Works, but TLE
    def lengthOfLongestSubstringTLE(self, s):
        longest = 0

        for i in range(len(s)):
            current = set(s[i])
            for j in range(i + 1, len(s)):
                if not s[j] in current:
                    current.add(s[j])
                else:
                    break
            longest = max(len(current), longest)
        
        return longest


### TESTING
#testStr = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"
Solution().lengthOfLongestSubstring("pwwkew")