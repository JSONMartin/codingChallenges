"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = {}; results = []

        for idx in range(len(s) - 9):
            subStr = s[idx:idx + 10]
            seen[subStr] = seen.get(subStr, 0) + 1
        
        for s in seen:
            if seen[s] > 1: results.append(s)
            
        return results

    def findRepeatedDnaSequencesTLE(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count = 0
        found = set()

        for idx in range(len(s) - 8):
            subStr = s[idx:idx + 10]
            checkStr = s[idx + 1:]

            if subStr in checkStr:
                count += 1
                found.add(subStr)
        
        return list( found )

### TESTING ###
#testStr ="AAAAAAAAAAA"
testStr = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Solution().findRepeatedDnaSequences(testStr)
