def matrixElementsSumHorizontalSolution(matrix):
    height, width = len(matrix), len(matrix[0])
    total = 0
    rowsToSkip = {}

    for row in range(height):
        for col in range(width):
            if matrix[row][col] == 0:
                rowsToSkip[col] = True
            if col in rowsToSkip:
                continue

            total += matrix[row][col]

    return total


def matrixElementsSumVerticalSolution(matrix):
    height, width = len(matrix), len(matrix[0])
    total = 0

    for col in range(width):
        for row in range(height):
            if matrix[row][col] == 0:
                break

            total += matrix[row][col]

    return total



# TESTS
matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

res = matrixElementsSum(matrix)  # ==> 9
print(res)
