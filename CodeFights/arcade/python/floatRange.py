from itertools import count, takewhile


def floatRange(start, stop, step):
    gen = takewhile(lambda n: n < stop, count(start, step))
    return list(gen)
