# UNSOLVED (I figured out solution but times out, need to implement "sliding window" strategy)
# https://leetcode.com/problems/find-all-anagrams-in-a-string/#/solutions
from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length = len(p)
        results = []
        pCount = Counter(p)
        
        print(pCount)

        memo = {}
        def isAnagram(subStr):

            return Counter(subStr) == pCount
            if subStr in memo: return memo[subStr]
            memo[subStr] = Counter(subStr) == pCount
            return memo[subStr]

            # subStrCount = Counter(subStr)
            # for el in pCount:
            #     if subStrCount[el] != pCount[el]:
            #         memo[subStr] = False
            #         return memo[subStr]
            # memo[subStr] = True
            # return memo[subStr]

        for i in range(len(s)):
            subStr = s[i:i+length]
            if len(subStr) < length: break
            elif isAnagram(subStr): results.append(i)
            print(subStr)

        return results

    # Works, but TLE
    def findAnagramsTLE(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        length = len(p)
        results = []
        #pCount = Counter(p)
        pSorted = ''.join(sorted(p))
        print(pSorted)

        for i in range(len(s)):
            subStr = s[i:i+length]
            if len(subStr) < length: break
            elif ''.join(sorted(subStr)) == pSorted: results.append(i)
            print(subStr)
        
        return results

res = Solution().findAnagrams("haha", "ha")

print(res)
