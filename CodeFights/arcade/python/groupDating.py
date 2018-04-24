def groupDating(male, female):
    return [[male[idx] for idx in range(len(male)) if male[idx] != female[idx]], [female[idx] for idx in range(len(male)) if male[idx] != female[idx]]]


""" TESTS """
male = [5, 28, 14, 99, 17]
female = [5, 14, 28, 99, 16]
res = groupDating(male, female)
print(res)
