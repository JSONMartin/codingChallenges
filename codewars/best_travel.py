# https://www.codewars.com/kata/best-travel/train/python
"""
John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible - to please Mary - but less than t - to please John- ?

Example:

With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language. With C++, C, Rust, Swift, Go return -1.

Examples:

ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, Rust, Swift, Go)

ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228
"""
indicies = {}

def generate_all_indicies(sofar, n, length, limit, results):
    if n >= limit:
        result_set = set(sofar)
        if len(set(sofar)) == len(sofar):
            #print("All uniques:", sofar)
            results[str(result_set)] = sofar[:]
            return sofar
        #else:
            #print("not unique, not adding:", sofar)
    else:
        for i in range(n, length):
            generate_all_indicies(sofar + [i], n + 1, length, limit, results)

#generate_all_indicies([], 0, 5, 3, {})
#print(results)

def choose_best_sum(total, num_towns, distances):
    def calc_total(indexes):
        sum = 0
        for index in indexes:
            sum += distances[index]
        return sum

    indexes = {}
    generate_all_indicies([], 0, len(distances), num_towns, indexes)
    print(len(indexes))

    print(indexes)


    results = []

    for idx_set in indexes:
        print(indexes[idx_set])
        idx_set_total = (calc_total(indexes[idx_set]))
        #print(total)
        difference = total - idx_set_total
        if difference == 0: return total
        elif difference < 0: continue
        else: results.append((difference, idx_set_total))

    results.sort()
    print(sorted(results))
    return results[0][1]


# def choose_best_sum(total, num_towns, distances):
#     #pointers = list(reversed([len(distances) - i - 1 for i in range(num_towns)]))
#     pointers = [i for i in range(num_towns)]
#     print(pointers)
#
#     totals = {}
#
#     def calc_total(indexes):
#         sum = 0
#         for index in indexes:
#             sum += distances[index]
#         return sum
#
#     pointer_combinations = []
#
#     while pointers[0] < num_towns:
#         for i in range(1, len(distances) - 1):
#             idx = (-i)
#             original_val = pointers[idx]
#             for j in range(original_val, len(distances)):
#                 #print(j)
#                 pointers[idx] = j
#                 #pointers[i-1] += 1
#                 print(pointers)
#
#             pointers[idx] = original_val + 1
#             #pointers[-1 -i] = original_val + 1
#             #pointers[1] += 1
#
#
#     #res = calc_total(pointers)
#     #print(res)
#
#     ## Generate Index Pairs
#
#     # while pointers[-1] > num_towns - 1:
#     #     for i in range(len(pointers)):
#     #         pointer = pointers[i]
#     #
#     #         for j in range(pointer + 1):
#     #             print(j)
#     #             pointers[i] = j
#     #             print("Adding:", pointers)
#     #             combination_total = calc_total(pointers)
#     #             if combination_total == total:
#     #                 print("Exact match found!", combination_total, pointers)
#     #                 return combination_total
#     #             else: totals[str(pointers)] = calc_total(pointers)
#     #
#     #         pointers[i] = pointer
#     #     # for p, idx in enumerate(pointers):
#     #     #     print(p, idx)
#     #         # for i in range(idx):
#     #             # print(p, idx)
#     #
#     #
#     #     pointers[-1] -= 1
#
#     #print(totals)
#
#
#     #while pointers[0] < num_towns - 1:
#
#
#
#     distances = sorted(distances)
#     print(distances)


### TESTING
from Test.Test import Test
t1 = [50, 55, 56, 57, 58]


#Test.assert_equals(choose_best_sum(163, 3, t1), 163)
#Test.assert_equals(choose_best_sum(174, 3, t1), 173)

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
#Test.assert_equals(choose_best_sum(230, 4, xs), 230)
#Test.assert_equals(choose_best_sum(430, 5, xs), 430)
Test.assert_equals(choose_best_sum(430, 8, xs), None)
