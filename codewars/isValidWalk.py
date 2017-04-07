def isValidWalk(walk):
    scores = {
        'n': 1,
        's': -1,
        'e': 2,
        'w': -2
    }

    total = 0

    for d in walk:
        total += scores[d]

    return total == 0

