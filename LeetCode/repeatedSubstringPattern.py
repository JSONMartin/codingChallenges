class Solution(object):
    def repeatedSubstringPattern(self, s):
        length = len(s)

        for i in xrange(1, length // 2 + 1):
            match = True
            subStr, remaining = s[:i], s[i:]
            subStrLength, remainingLength = len(subStr), len(remaining)

            for j in xrange(0, remainingLength, subStrLength):                
                if subStr != remaining[j: j + subStrLength]:
                    match = False
                    break

            if match: return True

        return False

s = Solution()
res = s.repeatedSubstringPattern("abab")
#res = s.repeatedSubstringPattern("aabaabaabaab")
#res = s.repeatedSubstringPattern("ababababab")
#res = s.repeatedSubstringPattern("abaababaab")

print(res)
