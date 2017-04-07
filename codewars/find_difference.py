from collections import Counter
class Solution(object):
    # Second Solution (Beats 30.03% of time)
    def findTheDifference(self, s1, s2):
        word1Count = Counter(s1)
        for ch in s2:
            if not ch in word1Count or word1Count[ch] <= 0: return ch
            else: word1Count[ch] -= 1

        return False

    # First Solution (Beats 6.03% of time)
    def findTheDifferenceFirst(self, s1, s2):
        word1Count = Counter(s1)
        word2Count = Counter(s2)
        result = list(word2Count - word1Count)
        print(result)
        return result[0]


s = Solution()
res = s.findTheDifference("abcd", "abcde")
print(res)

s.findTheDifference