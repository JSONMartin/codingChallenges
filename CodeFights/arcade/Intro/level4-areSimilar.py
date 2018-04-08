from collections import Counter


def areSimilar(a, b):
    length = len(a)

    # Ensure All characters match
    if Counter(a) != Counter(b):
        return False

    # Check for number of different elements at every index
    diffCount = 0

    for i in range(length):
        if a[i] != b[i]:
            diffCount += 1

    return diffCount <= 2


# TESTS
a = [1, 2, 3]
b = [2, 1, 3]
# a = [2, 1, 2, 1, 1, 1, 2]
#     [1, 1, 2, 1, 2, 1, 2]
# b = [1, 1, 2, 1, 2, 1, 2]
# a, b = [2, 2, 1], [2, 1, 1]
res = areSimilar(a, b)
print(res)
