from functools import reduce


def correctLineup(athletes):
    # result = reduce(lambda x, y: x + y, [(athletes[x + 1], athletes[x]) for x in range(0, len(athletes), 2)])
    result = [num for elem in [(athletes[x + 1], athletes[x]) for x in range(0, len(athletes), 2)] for num in elem]
    print(result)
    return result


""" TESTS """

correctLineup([1, 2, 3, 4, 5, 6])  # ==> [2, 1, 4, 3, 6, 5]
