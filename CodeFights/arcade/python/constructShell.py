def constructShell(n):
    return [[0] * i for i in range(1, n)] + [[0] * n] + [[0] * i for i in range(1, n)][::-1]
