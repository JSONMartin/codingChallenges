class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        def binary_search(arr, start, end):
            mid = int((start + end) / 2)

            if start > end: return -1

            if arr[mid] == B: return mid
            elif arr[mid] < B: return binary_search(arr, mid+1, end)
            else: return binary_search(arr, start, mid-1)

        def find_pivot(A, start, end):
            mid = int((start + end) / 2)

            if end < start: return False
            if end == start: return start

            if mid < end and A[mid] > A[mid+1]:
                return mid
            if mid > start and A[mid] < A[mid - 1]:
                return mid-1

            if A[start] >= A[mid]:
                return find_pivot(A, start, mid - 1)
            else:
                return find_pivot(A, mid + 1, end)

        pivot = find_pivot(A, 0, len(A) - 1)

        if not pivot:
            return binary_search(A, 0, len(A) -1)

        arr1 = A[0:pivot + 1]
        arr2 = A[pivot + 1:]
        result = None

        if arr1[0] <= B <= arr1[len(arr1) - 1]:
            result = binary_search(arr1, 0, len(arr1) -1)
        else:
            result = binary_search(arr2, 0, len(arr2) -1)
            if result > -1: result+= pivot + 1

        return result

##############
##############

s = Solution()
"""
TESTS
"""
#res = s.search([4, 5, 6, 7, 0, 1, 2], 5)
res = s.search([ 1, 7, 67, 133, 178 ], 1)
#res = s.search([ 19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17 ], 6)
print(res)