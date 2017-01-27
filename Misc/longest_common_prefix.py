class Solution(object):
    def longestCommonPrefix(self, strs):
        lcp = ""
        if not strs or len(strs) < 1: return lcp

        MIN_SIZE = min(map(len, strs))

        for i in range(MIN_SIZE):
            cur_letter = strs[0][i]

            for j in range(0, len(strs)):
                if strs[j][i] != cur_letter:
                    return lcp

            lcp+=cur_letter

        return lcp

#########
# TESTS #
#########
s = Solution()
#res = s.longestCommonPrefix(['aac', 'aab', 'aacd', 'alto'])
res = s.longestCommonPrefix(['a'])
print("RES:" + res)