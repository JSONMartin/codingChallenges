"""
Input: two n-digit positive integers x and y
Output: the product x · y
Assumption: n is a power of 2.

n = length of digits
"""

import math


def recIntMult(x, y):
    xDigits = str(x)
    yDigits = str(y)

    n = min(len(xDigits), len(yDigits))

    if len(xDigits) <= 1 or len(yDigits) <= 1:
        return x * y

    xMid = math.ceil(len(xDigits) / 2)
    yMid = math.ceil(len(yDigits) / 2)

    a, b = int(xDigits[:xMid]), int(xDigits[xMid:])
    c, d = int(yDigits[:yMid]), int(yDigits[yMid:])
    print(f"a:{a}, b:{b}, c:{c}, d:{d}")

    result = 10**n * recIntMult(a, c) + 10 ** (n / 2) * (recIntMult(a, d) + recIntMult(b, c)) + recIntMult(b, d)
    return int(result)


def KaratsubaMultiplication(x, y):
    xDigits, yDigits = str(x), str(y)
    length = min(len(xDigits), len(yDigits))

    if len(xDigits) <= 1 or len(yDigits) <= 1:
        return x * y

    # Set Mid point - if odd length, the longer digit needs to be in the first half,
    # rather than the second half. For example, `yMid = len(yDigits) // 2` won't work!
    xMid = math.ceil(len(xDigits) / 2)
    yMid = math.ceil(len(yDigits) / 2)

    a, b = int(xDigits[:xMid]), int(xDigits[xMid:])
    c, d = int(yDigits[:yMid]), int(yDigits[yMid:])
    p, q = (a + b), (c + d)
    ac = KaratsubaMultiplication(a, c)
    bd = KaratsubaMultiplication(b, d)
    pq = KaratsubaMultiplication(p, q)  # pq = p * q (use this line to debug if this doesn't work)

    adPlusbc = pq - ac - bd  # Stands for ad + bc ; equivlent to this code with 1 less recursive call: adbc = KaratsubaMultiplication(a, d) + KaratsubaMultiplication(b, c)
    result = ((10 ** length) * ac) + ((10 ** (length / 2)) * adPlusbc) + bd

    print(f"n (length): {length}, a: {a}, b: {b}, c: {c}, d: {d}, p: {p}, q: {q}, ac: {ac}, bd: {bd}, pq: {pq}, adbc:{adPlusbc}, result: {result}")
    return result


# Test Recursive Integer Multiplication
X, Y = 1111, 33333  # Result => 7006652
# X, Y = 1234, 5678  # Result => 7006652
# # X, Y = 1234, 5678
result = recIntMult(X, Y)
print(result)

# Test KaratsubaMultiplication
X, Y = 1234, 5678  # Result Should be => 7006652
result = KaratsubaMultiplication(X, Y)
print(result)
