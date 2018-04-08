def sudoku(grid):
    checkNumbers = lambda numbers: set(numbers) == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # Check Rows and Columns
    for n in range(len(grid)):
        row = [grid[n][colIdx] for colIdx in range(len(grid[0]))]
        col = [grid[rowIdx][n] for rowIdx in range(len(grid))]
        if checkNumbers(row) is False or checkNumbers(col) is False: return False

    # Check grids
    for colIdx in [0, 3, 6]:
        for rowIdx in [0, 3, 6]:
            subGrid = [grid[colIdx][rowIdx: rowIdx + 3], grid[colIdx + 1][rowIdx: rowIdx + 3], grid[colIdx + 2][rowIdx: rowIdx + 3]]
            subGrid = [number for sublist in subGrid for number in sublist]  # Flatten subGrid
            if checkNumbers(subGrid) is False: return False

    return True


""" TESTS """
res = sudoku([[1, 3, 2, 5, 4, 6, 9, 8, 7],
              [4, 6, 5, 8, 7, 9, 3, 2, 1],
              [7, 9, 8, 2, 1, 3, 6, 5, 4],
              [9, 2, 1, 4, 3, 5, 8, 7, 6],
              [3, 5, 4, 7, 6, 8, 2, 1, 9],
              [6, 8, 7, 1, 9, 2, 5, 4, 3],
              [5, 7, 6, 9, 8, 1, 4, 3, 2],
              [2, 4, 3, 6, 5, 7, 1, 9, 8],
              [8, 1, 9, 3, 2, 4, 7, 6, 5]])

print(res)
