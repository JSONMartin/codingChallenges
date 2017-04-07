"""
Your task, is to create a NxN spiral with a given size.

For example, spiral with size 5 should look like this:

00000
....0
000.0
0...0
00000
and with the size 10:

0000000000
.........0
00000000.0
0......0.0
0.0000.0.0
0.0..0.0.0
0.0....0.0
0.000000.0
0........0
0000000000
Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

[[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Because of the edge-cases for tiny spirals, the size will be at least 5.

General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.
"""
from Test.Test import Test

def printSpiral(spiral):
    print("---------------------------")
    for row in spiral: print(row)
    print("---------------------------")

def spiralize(size):
    # Base Cases
    if size == 0: return []
    elif size == 1: return [[1]]
    elif size == 2: return [[1, 1], [0, 1]]

    spiral = [[0] * size for i in range(size)]

    row, col = 0, 0
    start_row, start_col = None, None

    while (row, col) != (start_row, start_col):
        if row == size - 1 or col == size - 1 or spiral[row + 1][col + 1] == 1: break

        start_row, start_col = row, col
        moved = False

        # Top Left to Top Right (right)
        while col < size:
            if col + 1 < size and spiral[row][col + 1] == 1: break
            spiral[row][col] = 1
            col += 1
            moved = True
        if moved:
            col -= 1
            moved = False

        # Top Right to Bottom Right (down)
        while row < size:
            if row + 1 < size and spiral[row + 1][col] == 1: break
            spiral[row][col] = 1
            row += 1
            moved = True
        if moved:
            row -= 1
            moved = False

        # If completing next half of spiral will be incomplete, abort.
        if spiral[row - 1][col - 1] == 1: break

        # Bottom Right to Bottom Left (left)
        while col >= 0:
            if col - 1 >= 0 and spiral[row][col - 1] == 1: break
            spiral[row][col] = 1
            col -= 1
            moved = True
        if moved:
            col += 1
            moved = False

        # Bottom Left to Upper Left
        while row >= 0:
            if row - 1 >= 0 and spiral[row - 1][col] == 1: break
            spiral[row][col] = 1
            row -= 1
            moved = True
        if moved:
            row += 1

    return spiral

# def spiralize(size):
#     print(size)

#     elif size == 1: return [[1]]
#     elif size == 2: return [[1, 1], [0, 1]]
#     spiral = [[0] * size for i in range(size)]

#     def printSpiral():
#         print("---------------------------")
#         for row in spiral: print(row)
#         print("---------------------------")

#     printSpiral()

#     row, col = 0, 0
#     start_row, start_col = None, None

#     while (row, col) != (start_row, start_col):
#         if row == size - 1 or col == size - 1 or spiral[row + 1][col + 1] == 1: break
#         start_row, start_col = row, col
#         moved = False
#         # TL to TR (right)
#         while col < size:
#             #if col + 2 < size and spiral[row][col + 2] == 1: break
#             if col + 1 < size and spiral[row][col + 1] == 1: break
#             spiral[row][col] = 1
#             col += 1
#             moved = True

#         if moved:
#             col -= 1
#             moved = False

#         printSpiral()

#         # TR to BR (down)
#         while row < size:
#             #if row + 2 < size and spiral[row + 2][col] == 1: break
#             if row + 1 < size and spiral[row + 1][col] == 1: break
#             spiral[row][col] = 1
#             row += 1
#             moved = True
#         if moved:
#             row -= 1
#             moved = False

#         printSpiral()

#         # BR TO BL (left)
#         while col >= 0:
#             #if col - 2 >= 0 and spiral[row][col - 2] == 1: break
#             if col - 1 >= 0 and spiral[row][col - 1] == 1: break
#             spiral[row][col] = 1
#             col -= 1
#             moved = True
#         if moved:
#             col += 1
#             moved = False

#         printSpiral()

#         # BL TO UL
#         while row >= 0:
#             #if row - 2 > 0 and spiral[row - 2][col] == 1: break
#             if row - 1 >= 0 and spiral[row - 1][col] == 1: break
#             spiral[row][col] = 1
#             row -= 1
#             moved = True
#         if moved:
#             row += 1
#             moved = False

#         printSpiral()

#     return spiral


# def spiralize(size):
#     spiral = [[0] * size for i in range(size)]
#     possible_path = True
#
#     def checkSquare(row, col):
#         try: return spiral[row][col] != 1
#         except: return True
#
#     def visitCol(row, col):
#         nonlocal possible_path
#         possible_path = True
#         spiral[row][col] = 1
#
#     def printSpiral():
#         print("---------------------------")
#         for row in spiral: print(row)
#         print("---------------------------")
#
#
#     printSpiral()
#
#     x, y = 0, 0
#
#     #Loop through spiral
#     for i in range(2):
#         possible_path = False
#         printSpiral()
#
#         while x < size:
#             spiral[y][x] = 1
#             try:
#                 if spiral[y][x + 1] == 1: spiral[y][x] = 0
#                 x += 1
#             except:
#                 break
#
#         while y < size:
#             spiral[y][x] = 1
#             try:
#                 if spiral[y + 1][x] == 1: spiral[y][x] = 0
#                 y += 1
#             except:
#                 break
#
#         while x >= 0:
#             spiral[y][x] = 1
#             try:
#                 if x - 1 < 0: break
#                 elif spiral[y][x - 1] == 1: spiral[y][x] = 0
#                 x -= 1
#             except:
#                 x += 1
#                 break
#
#         while y >= 0:
#             spiral[y][x] = 1
#             try:
#                 if y - 1 < 0: break
#                 elif spiral[y - 1][x] == 1: spiral[y][x] = 0
#                 y -= 1
#             except:
#                 y += 1
#                 break
#
#     printSpiral()
#
#     # while possible_path:
#     #     possible_path = False
#     #     # Top Left to Top Right (Right)
#     #     while checkSquare(y, x + 1) and checkSquare(y, x + 2):
#     #         if x >= size:
#     #             x -= 1
#     #             break
#     #         else:
#     #             visitCol(y, x)
#     #             x += 1
#     #
#     #
#     #     # Top Right to Bottom Right (Down)
#     #     while checkSquare(y + 1, x) and checkSquare(y + 2, x):
#     #         if y >= size:
#     #             y -= 1
#     #             break
#     #         else:
#     #             visitCol(y, x)
#     #             y += 1
#     #
#     #     # Bottom Right to Bottom Left (Left)
#     #     while checkSquare(y, x - 1) and checkSquare(y, x - 2):
#     #         if x < 0:
#     #             x += 1
#     #             break
#     #         else:
#     #             visitCol(y, x)
#     #             x -= 1
#     #
#     #
#     #     # Bottom Left to Top Left (Up)
#     #     while checkSquare(y - 1, x) and checkSquare(y - 2, x):
#     #         if y < 0:
#     #             y += 1
#     #             break
#     #         else:
#     #             visitCol(y, x)
#     #             y -= 1
#
#     printSpiral()
#     # Make a snake
#     return spiral

#
# Test.assert_equals(spiralize(1), [[1]])
# Test.assert_equals(spiralize(2), [[1,1],
#                                   [0,1]])
# Test.assert_equals(spiralize(3), [[1,1,1],
#                                   [0,0,1],
#                                   [1,1,1]])
# #
# Test.assert_equals(spiralize(5), [[1,1,1,1,1],
#                                   [0,0,0,0,1],
#                                   [1,1,1,0,1],
#                                   [1,0,0,0,1],
#                                   [1,1,1,1,1]])

Test.assert_equals(spiralize(8), [[1,1,1,1,1,1,1,1],
                                  [0,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,0,1],
                                  [1,0,0,0,0,1,0,1],
                                  [1,0,1,0,0,1,0,1],
                                  [1,0,1,1,1,1,0,1],
                                  [1,0,0,0,0,0,0,1],
                                  [1,1,1,1,1,1,1,1]])


#spiralize(6)
# Failed for size 6:
#     [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]
#     should equal
#     [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 1], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1]]