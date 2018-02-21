def shapeArea(n):
    wholeSquare = ((2 * n) - 1) ** 2
    missingSquares = (((n ** 2) - n) / 2) * 4
    return wholeSquare - missingSquares


def shapeAreaSimplified(n):
    return (n ** 2) + ((n - 1) ** 2)
