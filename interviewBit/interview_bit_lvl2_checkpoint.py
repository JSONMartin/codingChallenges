class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        width = (2*A) - 1
        height = (2*A) - 1

        matrix = []
        for i in range(height):
            row = [0] * width
            matrix.append(row)
        print(matrix)

        center = (width/2)
        matrix[center][center] = 1

        for i in range(2, A + 1):
            cur_length = (2*i) - 1
            cur_bounds = width - cur_length

            #Go around in a clockwise motion, from:

            #Top Left to Top Right
            for j in range(cur_length):
                matrix[0 - i - center][j + cur_bounds - center + (i - 1)] = i

            #Top Right to Bot Right
            for j in range(cur_length):
                #print ("Top Right to Bot Right, i:%d, j:%d, center:%d, cur_bounds:%d" % (i, j, center, cur_bounds))
                matrix[center - j + i - 1][width - (cur_bounds / 2)- 1] = i

            #Bot Right to Bot Left
            for j in range(cur_length):
                #print ("Bot Left to Bot Right, i:%d, j:%d, center:%d" % (i, j, center))
                matrix[center + (i - 1)][j + cur_bounds - center + (i - 1)] = i

            #Bot Left to Upper Left
            for j in range(cur_length):
                #print ("Top Right to Bot Right, i:%d, j:%d, center:%d, cur_bounds:%d" % (i, j, center, cur_bounds))
                matrix[center - j + i - 1][0 + (cur_bounds / 2)] = i

        # str_print = ""
        #
        # for row in matrix:
        #     for num in row:
        #         str_print+=str(num) + " "
        #     str_print += "\n"
        #
        # print(str_print)


        #print(matrix)
        return matrix

"""
TESTS
"""

s = Solution()
result = s.prettyPrint(3)
print result