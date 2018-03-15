def boxBlur(image):
    rows, cols = len(image), len(image[0])

    blurred = []

    for row in range(1, rows - 1):
        blurredRow = []

        for col in range(1, cols - 1):
            total = sum([sum(image[row - 1][col - 1: col + 2]), sum(image[row][col - 1: col + 2]), sum(image[row + 1][col - 1: col + 2])])
            blurredRow += [total // 9]

        blurred += [blurredRow]

    return blurred


""" TESTS """

image = [
    [1, 1, 1],
    [1, 7, 1],
    [1, 1, 1],
]

image = [[7, 4, 0, 1],
         [5, 6, 2, 2],
         [6, 10, 7, 8],
         [1, 4, 2, 0]]

boxBlur(image)
