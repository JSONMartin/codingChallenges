class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        low = 0
        high = len(A) - 1
        mid = 0

        if B < A[low]: return 0
        if B > A[high]: return high + 1

        while low <= high:
            mid = int((high + low) / 2)
            print("Mid:%d, A[mid]:" % mid, A[mid])
            if A[mid] == B:
                return mid
            elif A[mid] > B:
                if A[mid - 1] < B: return mid
                high = mid - 1
            else:
                low = mid + 1

        return mid


##############

##############


