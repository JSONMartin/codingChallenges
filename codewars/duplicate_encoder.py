from collections import Counter

def duplicate_encode(word):
    word = word.lower()
    c = Counter(word)
    return "".join([')' if c[i] > 1 else '(' for i in word])

res = duplicate_encode("aasdAf")
print(res)