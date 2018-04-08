def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if i not in s:
            found = i
            break
    else:
        return upperBound

    return found
