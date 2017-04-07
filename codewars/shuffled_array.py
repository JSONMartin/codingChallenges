# https://www.codewars.com/kata/589573e3f0902e8919000109/train/python

def shuffled_array(s):
    total = sum(s)

    for num in s:
        if total - num == num:
            s.pop(s.index(num))
            break

    return sorted(s)



# First solution
# def shuffled_array(s):
#     addedSumIdx = 0
#
#     for i in range(len(s)):
#         others = s[:i] + s[i + 1:]
#         #print(others)
#         if s[i] == sum(others):
#             addedSumIdx = i
#             break
#
#     s.pop(addedSumIdx)
#     s.sort()
#     return s


### TESTS
shuffled_array([1, 12, 3, 6, 2])