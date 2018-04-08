def chessBoardCellColor(cell1, cell2):
    board = [[None] * 8 for n in range(8)]

    # Generate Checkerboard pattern
    whiteSquare = False

    for row in board:
        for idx, square in enumerate(row):
            row[idx] = whiteSquare
            whiteSquare = not whiteSquare
        whiteSquare = not whiteSquare

    # Convert Input into Matrix location
    location1 = (ord(cell1[0]) - ord('A'), int(cell1[1]) - 1)
    location2 = (ord(cell2[0]) - ord('A'), int(cell2[1]) - 1)

    # Return results
    return board[location1[1]][location1[0]] == board[location2[1]][location2[0]]


""" TESTS """
# res = chessBoardCellColor('A1', 'H3') # ==> False
# res = chessBoardCellColor('A1', 'C3')  # ==> True
res = chessBoardCellColor('A1', 'A2')  # ==> False
print(res)
