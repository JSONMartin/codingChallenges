def multiplicationTable(n):
    return [[row * col for col in range(1, n + 1)] for row in range(1, n + 1)]
