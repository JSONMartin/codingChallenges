"""
Input: two n-digit positive integers x and y
Output: the product x · y
Assumption: n is a power of 2.

n = length of digits
"""


def recIntMult(x, y):
    xDigits = str(x)
    yDigits = str(y)
    n = len(xDigits)

    if n == 1:  # base case
        return x * y

    a, b = int(xDigits[:n // 2]), int(xDigits[n // 2:])
    c, d = int(yDigits[:n // 2]), int(yDigits[n // 2:])
    print(f"a:{a}, b:{b}, c:{c}, d:{d}")

    result = 10**n * recIntMult(a, c) + 10 ** (n / 2) * (recIntMult(a, d) + recIntMult(b, c)) + recIntMult(b, d)
    return int(result)


# X, Y = 1234, 5678  # Result => 7006652
# # X, Y = 1234, 5678
# result = recIntMult(X, Y)
# print(result)


# def KaratsubaMultiplication(x, y):
#     xDigits, yDigits = str(x), str(y)
#     length = min(len(xDigits), len(yDigits))

#     # if length == 1:
#     # if len(xDigits) == 1 and len(yDigits) == 1:
#     if len(xDigits) <= 1 or len(yDigits) <= 1:
#         return x * y

#     mid = length // 2
#     if mid == 0:
#         mid = 1

#     a, b = int(xDigits[:mid]), int(xDigits[mid:])
#     c, d = int(yDigits[:mid]), int(yDigits[mid:])
#     p, q = a + b, c + d
#     print(a, b, c, d, p, q)
#     ac = KaratsubaMultiplication(a, c)
#     bd = KaratsubaMultiplication(b, d)
#     # pq = p * q
#     pq = KaratsubaMultiplication(p, q)

#     adbc = pq - ac - bd

#     result = (10 ** length) * ac + (10 ** (length / 2)) * adbc + bd
#     return result

def KaratsubaMultiplication(x, y):
    xDigits, yDigits = str(x), str(y)
    length = min(len(xDigits), len(yDigits))

    # if length == 1:
    # if len(xDigits) == 1 and len(yDigits) == 1:
    if len(xDigits) <= 1 or len(yDigits) <= 1:
        return x * y

    mid = length // 2
    if mid == 0:
        mid = 1

    a, b = int(xDigits[:mid]), int(xDigits[mid:])
    c, d = int(yDigits[:mid]), int(yDigits[mid:])
    p, q = a + b, c + d
    print(a, b, c, d, p, q)
    ac = KaratsubaMultiplication(a, c)
    bd = KaratsubaMultiplication(b, d)
    # pq = p * q
    pq = KaratsubaMultiplication(p, q)

    adbc = pq - ac - bd

    result = (10 ** length) * ac + (10 ** (length / 2)) * adbc + bd
    return result


# X, Y = 12345678, 87654321
X, Y = 1234, 5678  # Result => 7006652
result = KaratsubaMultiplication(X, Y)
print(result)
