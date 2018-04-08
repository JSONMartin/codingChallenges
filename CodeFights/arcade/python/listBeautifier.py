def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        start, *res, end = res
    return res
