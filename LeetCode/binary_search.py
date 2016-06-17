class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        def binarySearch(start, end):
            nonlocal A
            mid = round((end+start) / 2)
            print("Mid:%d" % mid)

            print("Mid ** 2:%d, A:%d" % (mid ** 2, A))

            if ((mid - 1) ** 2 < A) and mid ** 2 > A:
                print("Result found, mid:%d" % (mid - 1))
                return mid - 1

            if mid ** 2 == A: # check one left
                print("Result found, mid:%d" % mid)
                return mid

            if (mid-1) ** 2 == A: # check one right
                print("Result found, mid:%d" % mid - 1)
                return mid - 1

            if (mid + 1) ** 2 == A:  # check one right
                print("Result found, mid:%d" % mid + 1)
                return mid + 1

            if mid ** 2 > A:
                return binarySearch(start, mid - 1)
            elif mid ** 2 < A:
                return binarySearch(mid+1, end)

        return binarySearch(1, A)



        # if A == 0: return 0

        # for a in range(1, int(A/2)):
        #     if a**2 == A: return a
        #     if a**2 > A: return a - 1
        #
        #

    def sqrt_newton(self, A):
        return (A**(1/2))



        # if A == 0: return 0

        # for a in range(1, int(A/2)):
        #     if a**2 == A: return a
        #     if a**2 > A: return a - 1
        #
        #




##############
##############

s = Solution()
"""
TESTS
"""
#result = s.sqrt(11)
#result = s.sqrt(16)
result = s.sqrt_newton(4)
print("RES:%d" % result)