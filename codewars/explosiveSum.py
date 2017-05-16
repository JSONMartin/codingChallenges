"""
In number theory and combinatorics, a partition of a positive integer n, also called an integer partition, is a way of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition. If order matters, the sum becomes a composition. For example, 4 can be partitioned in five distinct ways:

4
3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1
"""

def memoize(fn):
    memo = {}

    def wrapper(comboSoFar, remaining):
        #key = str(comboSoFar) + "-" + str(remaining)
        key = str(comboSoFar)
        if key in memo:
            print("cache hit!", memo)
            return memo[key]
        memo[key] = fn(comboSoFar, remaining)
        return memo[key]

    return wrapper

# Dynamic Programming approach
def exp_sum_dp(n):
    dp = [0] + [1] * n
    nums = list(range(2, n + 1))

    for num in nums:
        for i in range(num, n + 1):
            dp[i] += dp[i - num] if dp[i - num] > 0 else 1

    return dp[-1]

# Memoized approach
memo = {}
def exp_sum(total, current = 1):
    if current > total: return 0
    if current == total: return 1
    
    key = (total, current)
    if key in memo: return memo[key]
    memo[key] = exp_sum(total - current, current) + exp_sum(total, current + 1)
    return memo[key]

# def exp_sum(n):
#     nums = [i for i in range(1, n + 1)]
#     LENGTH = len(nums)

#     @memoize
#     def findCombos(total, index):
#         if index >= LENGTH: return 0
#         curNum = nums[index]
#         #print(total, index, curNum)
#         ways = 0
        
#         if total == n: return 1
#         if total > n: return 0

#         #ways += findCombos(total, index + 1)
#         #ways += findCombos(total + curNum, index)
#         while total < n:
#             total += curNum
#             ways += findCombos(total, index + 1)
            
        
#         return ways
    
#     return findCombos(0, 0)
    
# def exp_sum(n):
#     combinations = [[n]]
#     memo = {}

#     def generateCombo(comboSoFar, curNum, remaining):
#         total = sum(comboSoFar)
#         # Caching
#         key = str(curNum) + "-" + str(remaining)
#         print(key)
#         # key = str(total) + "-" + str(remaining) + str(comboSoFar)
#         if key in memo:
#             print("Cache hit")
#             return memo[key]

#         if total == n:
#             #memo[]
#             combinations.append(comboSoFar[:])
#             memo[key] = memo.get(key, 0) + 1
#             return memo[key]
#             #return 1
#         if total > n:
#             #return 0
#             memo[key] = memo.get(key, 0)
#             return memo[key]

#         generateCombo(comboSoFar + [curNum], curNum, remaining[:])
#         if len(remaining) > 1: generateCombo(comboSoFar, remaining[0], remaining[1:])
        

#     nums = [i for i in range(1, n + 1)]
#     print(nums)
#     generateCombo([], nums[0], nums[1:])
#     print(combinations, " | Length: ", len(combinations))
#     print("------------")
#     print(memo)

# # Bottom Up
# # def exp_sum(n):
#     current = [1] * n
#     results = {
#         tuple(current): True
#     }
#     print(results)

#     def generateCombination(current):
#         if len(current) <= 1: return

#         left = [current[0] + current[1]] + current[2:]
#         right = [current[-1] + current[-2]] + current[0:-2]
#         #print(left, right)
#         results[tuple(sorted(left))] = True; results[tuple(sorted(right))] = True
#         generateCombination(left)
#         generateCombination(right)

    
#     generateCombination(current)
#     print(results)
#     print(len(results))


res = exp_sum(42)
print(res)
### TESTS ###
"""
test.describe('testing exp_sum')
test.it('***** Very basic tests *****\n')
test.assert_equals(exp_sum(-1), 0)
test.assert_equals(exp_sum(0), 1)
test.assert_equals(exp_sum(1), 1)
test.assert_equals(exp_sum(2), 2)
test.assert_equals(exp_sum(3), 3)
test.it('_____ So far so good _____\n')
test.it('\n***** Funcionality tests *****\n')
test.assert_equals(exp_sum(4), 5)
test.assert_equals(exp_sum(5), 7)
test.assert_equals(exp_sum(10), 42)
"""