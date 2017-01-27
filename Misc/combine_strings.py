def combine_strings(*strings):
    strs, result, done = list(map(list, strings)), "", False

    while not done:
        done = True

        for s in strs:
            if len(s) > 0:
                result += s.pop(0)
                done = False

    return result

############
# TESTS
############

res = combine_strings('abc', '123', 'blablabla')
print(res)