def bishopAndPawn(bishop, pawn):
    COLS = 'abcdefgh'
    ROWS = range(1, 9)
    possibilities = set()

    # Generate all Possibilities
    for col in COLS:
        if bishop[0] == col:
            continue
        difference = (abs(COLS.index(col) - COLS.index(bishop[0])))

        # Calculate the above and below diagnoal positions
        higher, lower = (col + str(int(bishop[1]) + difference)), (col + str(int(bishop[1]) - difference))
        for position in higher, lower:
            if int(position[1:]) > 0:
                possibilities.add(position)

    return pawn in possibilities


""" TESTING """
bishopAndPawn("d4", None)
