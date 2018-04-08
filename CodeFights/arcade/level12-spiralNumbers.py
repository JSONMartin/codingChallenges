"""
Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

spiralNumbers(n) = [[1, 2, 3],
                    [8, 9, 4],
                    [7, 6, 5]]
"""


def spiralNumbers(n):
    matrix = [[0] * n for row in range(n)]
    row, col = 0, 0
    counter = 1

    def fillDirection(direction):
        nonlocal row
        nonlocal col
        nonlocal counter
        try:
            if direction == 'R':
                while matrix[row][col] == 0:
                    matrix[row][col] = counter
                    col += 1
                    counter += 1
            if direction == 'D':
                row += 1
                col -= 1
                while matrix[row][col] == 0:
                    matrix[row][col] = counter
                    row += 1
                    counter += 1
            if direction == 'L':
                row -= 1
                col -= 1
                while matrix[row][col] == 0:
                    matrix[row][col] = counter
                    col -= 1
                    counter += 1
            if direction == 'U':
                row -= 1
                col += 1
                while matrix[row][col] == 0:
                    matrix[row][col] = counter
                    row -= 1
                    counter += 1
        except Exception:
            pass  # Out of Bounds

    while counter <= n ** 2:
        fillDirection('R')
        fillDirection('D')
        fillDirection('L')
        fillDirection('U')
        col += 1
        row += 1

    return matrix


""" TESTS """
spiralNumbers(3)
