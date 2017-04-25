from collections import Counter

class Solution(object):
    def isIsomorphic(self, a, b):
        def convertToUniqueCodes(string):
            counter = 0
            aSeen = {}
            aScanned = ""
            for ch in string:
                if ch in aSeen:
                    pass
                else:
                    aSeen[ch] = counter
                    counter += 1
                aScanned += str(aSeen[ch])
            return aScanned

        aScanned = convertToUniqueCodes(a); bScanned = convertToUniqueCodes(b)
        return aScanned == bScanned

#Solution().isIsomorphic("egg", "add")
res = Solution().isIsomorphic("paper", "title")
print(res)