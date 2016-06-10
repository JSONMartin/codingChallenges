# Island Count

"""
0  1  0  1  0
0  0  1  1  1
1  0  0  1  0
0  1  1  0  0
1  0  1  0  1
"""

def island_count(matrix):
    height = len(matrix)
    width = len(matrix[0])
    num_islands = 0

    def print_row(matrix):
        print_str = ""
        for row in range(height):
            row_str = ""
            for col in range(width):
                row_str+=str(matrix[row][col])
            print_str += row_str + "\n"
        print(print_str)

    def is_valid_position(matrix, row, col):
        if (0 < row < height) and (0 < col < width) and matrix[row][col] == 1: return True
        else: return False

    def expand_island(matrix, row, col):
        matrix[row][col] = 2
        # Check Up
        if (is_valid_position(matrix, row - 1, col)): expand_island(matrix, row-1, col)
        # Check Down
        if (is_valid_position(matrix, row + 1, col)): expand_island(matrix, row + 1, col)
        # Check Left
        if (is_valid_position(matrix, row, col - 1)): expand_island(matrix, row, col - 1)
        # Check Right
        if (is_valid_position(matrix, row, col + 1)): expand_island(matrix, row, col + 1)

    print("Before expanding:")
    print_row(matrix)

    # Scan row until 1 found, then expand island
    for row in range(height):
        for col in range(width):
            if(matrix[row][col] == 1):
                num_islands+=1
                expand_island(matrix, row, col) # Expand
                print("After expanding:")
                print_row(matrix)

    return num_islands



"""
Testing
"""
test_island = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
]

result = island_count(test_island)
print ("NumIslands result:%d" % result)




