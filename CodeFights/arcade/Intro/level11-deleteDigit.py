def deleteDigit(n):
    nStr = str(n)
    return max([int(nStr[:idx] + nStr[idx + 1:]) for idx in range(len(nStr))])


deleteDigit(152)
