"""
# https://www.codewars.com/kata/5432fd1c913a65b28f000342/train/python

Create a function that accepts dimensions, of Rows x Columns, as parameters in order to create a multiplication table sized according to the given dimensions. **The return value of the function must be an array, and the numbers must be Fixnums, NOT strings.

Example:

multiplication_table(3,3)

1 2 3
2 4 6
3 6 9

-->[[1,2,3],[2,4,6],[3,6,9]]

Each value on the table should be equal to the value of multiplying the number in its first row times the number in its first column.
"""
# Improved 1 liner solution
def multiplication_table(row_nums, col_nums):
    return [[(row + 1) * (col + 1) for col in range(col_nums)] for row in range(row_nums)]


# Original solution
def multiplication_table_og(row,col):
    table = [[None for c in range(col)] for r in range(row)]

    print(table)

    # Populate First Row
    for c in range(0, col):
        table[0][c] = c + 1

    # Populate First Column
    for r in range(0, row):
        table[r][0] = r + 1

    # Populate empty spaces in remaining rows
    for r in range(1, row):
        for c in range(1, col):
            table[r][c] = table[r][0] * table[0][c]

    print(table)

    return table

### TESTS ###
res = multiplication_table(6, 3)
print(res)