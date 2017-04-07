

class Solution(object):
    def kthSmallest(self, matrix, k):
        flattened = [item for matrix in matrix for item in matrix]
        return list(sorted(flattened))[k - 1]

### TESTING ###

s = Solution()
res = s.kthSmallest([
    [ 1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8)

print(res)

