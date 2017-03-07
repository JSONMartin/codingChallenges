"""
My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write a program that could help us and protects trees.

Task

Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language) of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return the result with the largest possible values:

Examples

decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11², 11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly increasing sequence.

Note

Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing, None (depending on the language) or "" (Java, C#) or {} (C++).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

[x1 ... xk]
Hint

Very often xk will be n-1.
"""

# https://www.codewars.com/kata/54eb33e5bc1a25440d000891/solutions/python

import math

def decompose(n):
    TOTAL_TO_EQUAL = n ** 2

    def generate_composition(current = [], sum = 0, start = n - 1):
        if sum == (n ** 2): return current # Match found
        elif sum > (n ** 2) or start <= 0: return False # Out of bounds or over total

        i = start

        while i >= 1:
            if (sum + (i ** 2)) <= TOTAL_TO_EQUAL:
                combo = generate_composition(current[:] + [i], sum + (i ** 2), i - 1)
                i -= 1

                if combo == False: generate_composition(current, sum, start - 1)
                elif combo: return combo
            else:
                i = math.floor(math.sqrt(TOTAL_TO_EQUAL - sum))

    result = generate_composition()

    try:
        return list(reversed(result))
    except:
        return None

def decomposeBeforeRefactor(n): # Original solution
    results = []

    def generate_composition(current = [], sum = 0, start = n - 1):
        if len(results) > 0: return results

        if sum == (n ** 2):
            results.append(current[:])
            return current

        elif sum > (n ** 2) or start <= 0:
            return False

        i = start

        while i >= 1:
            if len(results) > 0: return results
            if len(current) > 1 and i == current[-1]: return False

            if sum + (i ** 2) <= n ** 2:
                combo = generate_composition(current[:] + [i], sum + (i ** 2), i - 1)
                i -= 1

                if combo == False:
                    generate_composition(current, sum, start - 1)
                    break
                if combo == True:
                    print("Combo == True, should fire")
                    return results
            else:
                i = math.floor(math.sqrt(n ** 2 - sum))

    generate_composition()

    return sorted(results[0]) if len(results) > 0 else None



### TESTS ###
TEST_VAL = 123456
print("Original:\n")
res = decompose(TEST_VAL)
print(res)


print("Refactored:\n")
res = decomposeBeforeRefactor(TEST_VAL)
print(res)