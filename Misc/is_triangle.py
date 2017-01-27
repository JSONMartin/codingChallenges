def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        return (a + b > c) and (a + c > b) and (b + c > a)


### TESTS
print(is_triangle(0, 1, 2))