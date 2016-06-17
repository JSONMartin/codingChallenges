class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosestQuad(self, A, B): # Quadratic solution
        A.sort()
        n = len(A)

        min_diff = 999**99
        min_total = 999**99

        for i in range(n):
            print(A)
            a = A[i]
            start = i + 1
            end = n - 1

            while(start < end):
                b = A[start]
                c = A[end]

                total = a + b + c
                diff = abs(B - total)

                print("a:%d, b:%d, c:%d | start:%d, end:%d" % (a, b, c, start, end))
                print("TOtal:%d, diff:%d, min_diff:%d" % (total, diff, min_diff))
                print(" -- ")

                if diff < min_diff:
                    min_diff = diff
                    min_total = total
                end = end - 1
                #elif (diff < min_diff):
                    #end -= 1
                #elif
                #else: start+=1
                #end = end - 1

            start = i + 1
            end = n - 1
            while (start < end):
                b = A[start]
                c = A[end]

                total = a + b + c
                diff = abs(B - total)

                print("a:%d, b:%d, c:%d | start:%d, end:%d" % (a, b, c, start, end))
                print("TOtal:%d, diff:%d, min_diff:%d" % (total, diff, min_diff))
                print(" -- ")

                if diff < min_diff:
                    min_diff = diff
                    min_total = total
                start+=1

        #print("Min_diff:%d"%min_diff)
        #print("Min_elems")
        #print(min_total)
        return min_total






    def threeSumClosest(self, A, B):
        pair_sums = {}
        results = []

        ## Loop through array and total sum pairs
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                total = A[i] + A[j]
                pair_sums[total] = (i, j)
                #print((i, j)

        ## Loop through array again and calculate results
        for i in range(len(A)):
            for key in pair_sums.keys():
                if i not in pair_sums[key]: # Makes sure it's not checking with one of the already summed elements
                    total = A[i] + int(key)
                    total_tup = (total, ( A[pair_sums[key][0]], A[pair_sums[key][1]], A[i] ) )
                    results.append(total_tup)

        ## Calculate difference from B
        min_sum = float('inf')
        min_elem = None

        for r in results:
            total = r[0]
            elem_sum = r[1][0] + r[1][1] + r[1][2]
            closest_sum_to_target = abs(B - total)
            if closest_sum_to_target < min_sum:
                min_sum = closest_sum_to_target
                min_elem = elem_sum

        return min_elem

s = Solution()
"""
TESTS
"""
#res = s.threeSumClosest([-1, 2, 1, -4], 1)
res = s.threeSumClosestQuad([ 5, -2, -1, -10, 10 ], 5)
#res = s.threeSumClosestQuad([ -6, 1, -4, -1, 8, -4, 9, 0, -3, 7, -3, 2, -4, -2, 3, -4, 10, 0, 9, 6, 1, 3, 4, 2 ], -3)
#res = s.threeSumClosestQuad([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ], -1)
print(res)