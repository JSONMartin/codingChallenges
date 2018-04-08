def isLucky(n):
    nStr = str(n)
    mid = len(nStr) // 2
    left, right = [int(i) for i in nStr[:mid]], [int(i) for i in nStr[mid:]]

    return sum(left) == sum(right)


# TESTS
isLucky(1230)
