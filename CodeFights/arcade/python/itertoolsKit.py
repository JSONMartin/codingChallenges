from itertools import product


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return list(sorted(filter(lambda x: int(x) % d == 0, map(createNumber, product(digits, repeat=k)))))
