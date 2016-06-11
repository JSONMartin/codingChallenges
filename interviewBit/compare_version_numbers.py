class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        A = list('.'.join(list((map(lambda c: str(int(c)), (list(filter((lambda c: int(c)!=0), A.split('.')))))))).split('.'))
        B = list('.'.join(list((map(lambda c: str(int(c)), (list(filter((lambda c: int(c)!=0), B.split('.')))))))).split('.'))

        while len(A) > 0 and len(B) > 0:
            a = int(A.pop(0))
            b = int(B.pop(0))
            if a > b:
                return 1
            elif b > a:
                return -1

        if len(A) <= 0 and len(B) > 0: return -1
        elif len(B) <= 0 and len(A) > 0: return 1
        else: return 0

"""TESTS"""

s = Solution()

#res = s.compareVersion("1.13", "1.13.4")
#res = s.compareVersion("1.13.42.5", "1.13.43.4")
#res = s.compareVersion("01", "1")
# res = s.compareVersion("1.0", "1")
res = s.compareVersion("4444371174137455", "5.168")
print(res)