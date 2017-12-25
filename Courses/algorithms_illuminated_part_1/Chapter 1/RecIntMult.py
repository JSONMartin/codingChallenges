"""
Input: two n-digit positive integers x and y
Output: the product x · y
Assumption: n is a power of 2.

Multiplies by breaking up number into 2 half, a/b for x and c/d for y respectively.

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


X, Y = 1234, 5678  # Result => 7006652
# X, Y = 1234, 5678
result = recIntMult(X, Y)
print(result)
