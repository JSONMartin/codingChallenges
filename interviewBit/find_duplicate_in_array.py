class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        count_dict = {}
        for n in A:
            count_dict[n] = count_dict.get(n, 0) + 1
            if count_dict[n] > 1: return n
        #print(count_dict)

"""
TESTING
"""
s = Solution()

res = s.repeatedNumber([3, 4, 1, 4, 1])
print(res)