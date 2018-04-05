def chessKnight(cell):
    col = int(cell[1])
    row = int(ord(cell[0]) - ord('a')) + 1
    totalMoves = 0

    print(row, col)
    for rowDiff, colDiff in ((-1, -2), (-2, -1), (1, -2), (-2, 1), (-1, 2), (2, -1), (1, 2), (2, 1)):
        if row + rowDiff < 1 or row + rowDiff > 8 or col + colDiff > 8 or col + colDiff < 1:
            continue

        totalMoves += 1

    print("Total Moves:%d" % totalMoves)
    return totalMoves


""" TESTING """
chessKnight('a1')
