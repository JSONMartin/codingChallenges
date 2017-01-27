def accum(s):
    result, count = "", 0

    for ch in s:
        result += ch.upper() + (ch.lower() * count) + "-"
        count += 1

    return result[:-1]

### TESTS
res = accum("ZpglnRxqenU")
print(res)