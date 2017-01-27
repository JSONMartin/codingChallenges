def decrypt(text, n):
    if n <= 0: return text

    left, right, mid, result = "", "", len(text)//2, ""

    left, right = list(text[:mid]), list(text[mid:])

    while left and right:
        result += right.pop(0)
        result += left.pop(0)

    while right:
        result += right.pop(0)

    while left:
        result += left.pop(0)

    return decrypt(result, n - 1)

def encrypt(text, n):
    if n <= 0: return text

    left, right = "", ""

    for i in range(0, len(text)):
        if i % 2 == 0:
            right += text[i]
        else:
            left += text[i]

    return encrypt(left + right, n - 1)



res = encrypt("This is a test!", 2)
print(res)

res = decrypt(res, 2)
print(res)
