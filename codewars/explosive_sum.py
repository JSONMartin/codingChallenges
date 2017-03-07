"""
How many ways can you make the sum of a number?

From wikipedia: https://en.wikipedia.org/wiki/Partition_(number_theory)#

In number theory and combinatorics, a partition of a positive integer n,
also called an integer partition, is a way of writing n as a sum of positive integers.

Two sums that differ only in the order of their summands are considered the same partition.
If order matters, the sum becomes a composition.

For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
Examples

3
2 + 1
1 + 1 + 1

5
4 + 1
3 + 1 + 1
3 + 2
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

Trivial

sum(-1) # 0
sum(1) # 1
Basic

sum(2) # 2  -> 1+1 , 2
sum(3) # 3 -> 1+1+1, 1+2, 3
sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
sum(5) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
sum (6)
            #[[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [2, 2, 1, 1], [2, 3, 1], [3, 1, 1, 1], [3, 4], [4, 1, 1], [5, 1], [6]]
            #[[1, 1, 1, 1, 1, 1], [2, 1, 1, 1, 1], [2, 2, 1, 1], [2, 2, 2], [3, 1, 1, 1], [3, 2, 1], [3, 3], [4, 1, 1], [4, 2], [5, 1], [6]]

sum(10) # 42
Explosive

sum(50) # 204226
sum(80) # 15796476
sum(100) # 190569292
"""


# sum(4) # 5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
def exp_sum_FIRST(n):
    MAKE_COMBINATION_CALLS = 0

    if n < 0: return 0
    results = [[n]]

    memoized = {2: [[1, 1]], 3:[[1, 1, 1], [1, 2]]}


    # Bottom up
    def make_combination(n):
        combo = {}

        if n in memoized:
            return memoized[n]
        else:
            for i in range(n, n//2 - 1, -1):
                #combo.append([i, n - i])
                if n - i > 0:
                    combo[str([i, n - i])] = [i, n - i]
                else:
                    combo[str([i, n - i])] = [i]
                # last = [j for j in make_combination(n-1)
                last = make_combination(n-1)
                for combination in last:
                    print(combination)
                    new_combo = [1] + combination
                    combo[str(new_combo)] = new_combo
                print(last)

        memoized[n] = list(combo.values())
        return memoized[n]

    results = make_combination(n)

    results_sorted = sorted([sorted(item) for item in results])

    results_set = {}
    for result in results_sorted:
        print(result)
        results_set[str(result)] = result

    print("results_set:", results_set)


    #print("Make Combination Calls:%d" % MAKE_COMBINATION_CALLS)
    #print(memoized)
    TOTAL = sorted(list(results_set.values()))
    print("Results:\n", TOTAL)
    print("Results length:", len(TOTAL))
    #return len(results)


    ##################################################

    # results = [[1] * n]
    # print(results)

    # This combination does not work for larger numbers.

    # def make_combination(current = results[0][:], direction = 'right'):
    #     nonlocal MAKE_COMBINATION_CALLS
    #     MAKE_COMBINATION_CALLS += 1
    #
    #     if direction == 'right':
    #         current[-2] += current[-1]
    #         if sum(current[:-1]) == n: results.append(current[:-1])
    #     else:
    #         current[1] += current[0]
    #         if sum(current[1:]) == n: results.append(current[1:])
    #
    #     if len(current) > 3:
    #         make_combination(current[0:-1], 'right')
    #         make_combination(current[0:-1], 'left')

    #
    # # Alternative solution: try to do this from bottom up, instead of top down

    #memoized = {'[1, 1]': [2]}



    # def make_combination(current = [], cur_n = n - 1, total = 0):
    #     # Update call counter
    #     nonlocal MAKE_COMBINATION_CALLS
    #     MAKE_COMBINATION_CALLS += 1
    #
    #     # Check if already calculated
    #     if str((current, cur_n, total)) in memoized:
    #         return memoized[str((current, cur_n, total))]
    #
    #     if cur_n < 0 or total > n: return
    #
    #     if cur_n == 1 and total < n:
    #         make_combination(current + [cur_n], 1, total + cur_n)
    #         memoized[str((current, cur_n, total))] = current[:]
    #         return current[:]
    #
    #     else:
    #         if cur_n == n:
    #             results.append([cur_n])
    #         if total == n:
    #             results.append(current)
    #             memoized[str((current, cur_n, total))] = current[:]
    #             return current
    #
    #         make_combination(current + [cur_n], cur_n, total + cur_n)
    #         make_combination(current, cur_n - 1, total)

    # make_combination()
    #
    # print("Make Combination Calls:%d" % MAKE_COMBINATION_CALLS)
    # print(memoized)
    # print("Results:\n", sorted(results))
    # return len(results)

    #return result if result != None else 0

MAKE_COMBINATION_CALLS = 0
def exp_sum(n):
    global MAKE_COMBINATION_CALLS
    MAKE_COMBINATION_CALLS += 1
    if n < 0: return 0

    if n == 2: return [[1, 1], [2]]
    else:
        next = list([i + [1] for i in exp_sum(n-1)]) + [[n]]
        # if n > 3 and n-3 + n-2 == n: next += [[n-3, n-2]]
        # elif n > 3 and n-3 + n-3 == n: next += [[n-3, n-3]]
        if n > 3 and n - 2 + n - 2 == n: next += [[n-2, n-2]]
        elif n > 3: next += [[n-3, n-2]]
        # elif n > 3 : next += [[n-3, n-3]]

        return list(next)



def partition(number):
    return partitions_dp(number)
    # answer = set()
    # answer.add((number, ))
    # for x in range(1, number):
    #     for y in partition(number - x):
    #         answer.add(tuple(sorted((x, ) + y)))
    # return answer

def partitions_dp(n):
    partitions_of = []
    partitions_of.append([()])
    partitions_of.append([(1,)])
    for num in range(2, n+1):
        ptitions = set()
        for i in range(num):
            for partition in partitions_of[i]:
                ptitions.add(tuple(sorted((num - i, ) + partition)))
        partitions_of.append(list(ptitions))
    return partitions_of[n]

def exp_sum(n):
    if n < 0: return 0
    elif n == 0: return 1
    elif n == 1: return 1
    results = []

    for i in range(1, n):
        results.append(part(n, i))

    print(results)
    return len(results)

def part(n, k):
    def memoize(f):
        cache = [[[None] * n for j in range(k)] for i in range(n)]
        def wrapper(n, k, pre):
            if cache[n-1][k-1][pre-1] is None:
                cache[n-1][k-1][pre-1] = f(n, k, pre)
            return cache[n-1][k-1][pre-1]
        return wrapper

    @memoize
    def _part(n, k, pre):
        if n <= 0:
            return []
        if k == 1:
            if n <= pre:
                return [(n,)]
            return []
        ret = []
        for i in range(min(pre, n), 0, -1):
            ret += [(i,) + sub for sub in _part(n-i, k-1, i)]
        return ret
    return _part(n, k, n)

print(part(2, 2))

### TESTS
# res = exp_sum(6) # 2 -> 1+1 , 2
# #print(sorted(res))
# print(sorted(res))
# print("Length:", len(res))
# print("Make combination calls:", MAKE_COMBINATION_CALLS)
# #
# print("-----------------------");
# res = partition(50) # 2 -> 1+1 , 2
# # #print(sorted(res))
# print(res)
# print("Length:", len(res))