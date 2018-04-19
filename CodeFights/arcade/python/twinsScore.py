def twinsScore(b, m):
    return [b[i] + m[i] for i in range(len(b))]

    for x in b:
        print(b)
        print(l)
    # or..
    # return map(sum, zip(b, m))


### TESTS ###
b = [22, 13, 45, 32]
m = [28, 41, 13, 32]

twinsScore(b, m)
