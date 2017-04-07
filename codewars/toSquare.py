import math

def square_or_square_root(arr):
    print(arr)
    res = [int(math.sqrt(n)) if math.sqrt(n) == int(math.sqrt(n)) else int(n ** 2) for n in arr]
    return res

res = square_or_square_root([4, 3, 9, 7, 2, 1 ])
print(res)