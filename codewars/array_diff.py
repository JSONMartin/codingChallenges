def array_diff(a, b):
    result = []
    diff_dict = {}

    for n in b:
        diff_dict[n] = True

    for n in a:
        if n in diff_dict:
            pass
        else:
            result.append(n)

    return result

    # if len(a) == 0 or len(b) == 0: return []

    # if len(b) > len(a):
    #     for n in a:
    #         diff_dict[n] = True
    #
    #     for n in b:
    #         if n in diff_dict:
    #             pass
    #         else:
    #             result.append(n)
    # else:
    #     for n in b:
    #         diff_dict[n] = True
    #
    #     for n in a:
    #         if n in diff_dict:
    #             pass
    #         else:
    #             result.append(n)

    return result

a = [1, 2, 4]
b = [1, 3]

print array_diff(a, b)
print array_diff(a, [])
