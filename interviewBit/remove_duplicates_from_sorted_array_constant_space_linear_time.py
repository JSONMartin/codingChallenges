class Solution:
    # @param A : list of integers
    # @return an integer

    # This solution works in place and moves elements down,
    # rather than removing elements of array to save time complexity
    def removeDuplicates(self, A):
        i = 0
        j = 1

        counter = 1

        while j < len(A):
            if A[i] > A[j]: break

            if A[i] == A[j]:
                if j + 1 >= len(A): break

                while j + 1 < len(A) and A[j + 1] == A[j]:
                    j+=1

                if j + 1 < len(A):
                    A[i+1] = A[j+1]
                    counter += 1
                j+=1
                i+=1

            else:
                i+=1
                j+=1
                counter += 1
                
        return counter # The counter allows the correct array to be retrieved with A[:counter]

s = Solution()
#A = [1, 1, 2, 3, 3, 3, 5]
#A = [ 5000, 5000, 5000 ]
#A = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]
#A = [0]
A = [ 0, 1, 1, 2, 2, 3, 3, 3, 3 ]
res = s.removeDuplicates(A)
print res


