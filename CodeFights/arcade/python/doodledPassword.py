from collections import deque


def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda idx: res[idx].rotate(- idx), range(n)), 0)
    return [list(d) for d in res]
