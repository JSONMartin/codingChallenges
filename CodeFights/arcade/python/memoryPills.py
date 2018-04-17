from itertools import dropwhile

def memoryPills(pills):
    gen = dropwhile(lambda pill: len(pill) % 2, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]
