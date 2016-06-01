class Solution:
    # @param A : list of list of integers
    # @return the same list modified

    def rotate(self, arr):
        arr_size = len(arr)

        def swap(aRow, aCol, bRow, bCol, arr, val):
            tmp = arr[bRow][bCol]
            arr[bRow][bCol] = val
            return tmp

        for r in range((len(arr)) / 2):
            for i in range(len(arr) - 1 - r*2 ):
                start_val = arr[arr_size - i - r - 1][r]
                ## Swap Bottom Left to Top Left
                res = swap(arr_size - 1 - r - i, r, r, r+i, arr, start_val)
                ## Swap top left to top right
                res = swap(r, r+i, r+i, arr_size - 1 - r, arr, res)
                ## Swap top right to bottom right
                res = swap(r+i, arr_size - 1 - r, arr_size - 1 - r, arr_size - 1 - i - r, arr, res)
                ## Swap bottom right to bottom left
                res = swap(arr_size - 1 - r, arr_size - 1 - i - r, arr_size - 1 - i - r, r, arr, res)
        return arr

s = Solution()
#matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
#matrix = ([[1, 2],[3, 4],[5, 6]])
#matrix = ([[1, 2],[3, 4]])
#s.rotate([matrix])
#s.rotate([[1, 2],[3, 4]])
#s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#s.rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print s.rotate([[31, 32, 228, 333], [79, 197, 241, 246], [77, 84, 126, 337], [110, 291, 356, 371]])

# leng = len([[1, 2],[3, 4],[5, 6]])
# print leng