"""
In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, False, False],
          [False, true, False],
          [False, False, False]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]
"""


def minesweeper(matrix):
    rows, cols = len(matrix), len(matrix[0])
    resultMatrix = [[0] * cols for row in range(rows)]

    def mineCellScore(row, col):
        score = 0

        for rowOffset in [-1, 0, 1]:
            for colOffset in [-1, 0, 1]:
                rowPos, colPos = row + rowOffset, col + colOffset
                print(rowOffset, colOffset)

                if (rowOffset == 0 and colOffset == 0) or rowPos < 0 or rowPos >= rows or colPos < 0 or colPos >= cols:
                    continue  # Skip for current cell, or any out of bounds cells
                score += int(matrix[row + rowOffset][col + colOffset])

        return score

    # Calculate scores for each cell
    for row in range(rows):
        for col in range(cols):
            resultMatrix[row][col] = mineCellScore(row, col)

    return resultMatrix


""" TESTS """
# matrix = [[True, False, False],
#           [False, True, False],
#           [False, False, False]]
matrix = [
    [True, False, False, True],
    [False, False, True, False],
    [True, True, False, True]
]

res = minesweeper(matrix)
""" 
[[1, 2, 1],
[2, 1, 1],
[1, 1, 1]]
"""
print(res)
