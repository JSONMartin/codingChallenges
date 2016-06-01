class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, numRows):
        arr = []

        def generateRow(rowN, arr):
            if rowN == 1: arr.append([1])
            elif rowN == 2: arr.append([1, 1])
            else:
                curRowArr = [1]
                lastRowArr = arr[rowN - 2]
                for i in range(len(lastRowArr) - 1):
                    curRowArr.append(lastRowArr[i] + lastRowArr[i + 1])
                curRowArr.append(1)
                arr.append(curRowArr)

        for j in range(1, numRows + 1):
            generateRow(j, arr)

        return arr