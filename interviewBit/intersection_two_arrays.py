class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        result = []
        # A = list(A)
        # B = list(B)

        Adx = 0
        Bdx = 0

        while (Adx < len(A)) and (Bdx < len(B)):
            a = A[Adx]
            b = B[Bdx]
            if a == b:
                result.append(a)
                Adx+=1
                Bdx += 1
            elif a < b:
                Adx += 1
            elif b < a:
                Bdx += 1

        return result


s = Solution()

A = [1, 2, 3, 3, 4, 5, 6]
B = [3, 3, 5]


print s.intersect(A, B)

            # check A[0] against B[0]
                #if equal, push A[0] into result, and shift off A[0] and B[0]
                #elif a < b, shift off A[0]
                #elif b > a, shift off B[0]


