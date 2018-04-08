def differentSquares(matrix):
    uniqueSquares = set()

    for rowIdx in range(len(matrix) - 1):
        for colIdx in range(len(matrix[0]) - 1):
            subMatrix = (tuple(matrix[rowIdx][colIdx: colIdx + 2]), tuple(matrix[rowIdx + 1][colIdx: colIdx + 2]))
            uniqueSquares.add(subMatrix)

    return len(uniqueSquares)
    print(len(uniqueSquares))


""" TESTS """

res = differentSquares([[1, 2, 1],
                        [2, 2, 2],
                        [2, 2, 2],
                        [1, 2, 3],
                        [2, 2, 1]])

print(res)
