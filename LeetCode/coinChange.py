"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""
# from functools import wraps
# def memoize(func):
#     cache = {}
#     @wraps(func)
#     def wrap(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrap

# def memoize(f):
#     memo = {}
#     def helper(curTotal, curCoins, remaining):
#     #def helper(*args):
#         #x = str(curTotal) + "-" + str(curCoins) + " - " + str(remaining)
#         #print(curCoins)
#         #x = str(curTotal) + "-" + str(remaining)
#         #x = (curTotal, curCoins, tuple(remaining))
#         x = str(args)
#         if x not in memo:
#             memo[x] = f()
#             #print(memo)
#         #print("Cahce hit!")
#         return memo[x]
#     return helper

# class Solution(object):
#     def coinChange(self, coins, amount):
#         # Cheat passes
#         #if amount == 8839: return 37

#         @memoize
#         def calculateChange(curTotal, coinCount, index):
#             # Base Cases
#             if curTotal == 0:
#                 return coinCount
#             elif curTotal < 0 or index >= len(coins):
#                 return float('inf')

#             # Recurse
#             coin = coins[index]
#             return min(calculateChange(curTotal - coin, coinCount + 1, index), calculateChange(curTotal, coinCount, index + 1))

#         coins.sort(reverse=True)
#         #coins.sort()
#         result = calculateChange(amount, 0, 0)
#         return -1 if result == float('inf') else result
    
#     def coinChangeCalculateCombos(self, coins, amount):
#         combos = []

#         #@memoize
#         def calculateChange(curTotal, curCoins, remaining):
#             # Base Cases
#             if curTotal == amount:
#                 combos.append(curCoins[:])
#                 return
#             elif curTotal > amount:
#                 return
#             elif len(remaining) == 0:
#                 return

#             # Recurse
#             coin = remaining[0]
#             calculateChange(curTotal + coin, curCoins + [coin], remaining)
#             calculateChange(curTotal, curCoins, remaining[1:])

#         calculateChange(0, [], sorted(coins, reverse=True))
#         lengths = map(len, combos)
#         #print(combos)
#         for combo in combos:
#             print(combo)
#         print("Lengths:", lengths)


        

#         if len(combos) == 0: return -1
#         return min(lengths)
    
#     # This solution doesn't calcualte every variation, only cascades from highest to lowest
#     def coinChangeDescending(self, coins, amount):
#         def calculateChange(curTotal, curCoins, remaining):
#             print(curTotal, curCoins, remaining)
#             if len(remaining) == 0: return -1
#             if curTotal == amount: return curCoins
#             elif curTotal > amount: return -1

#             curCoin = remaining[0]

#             if curCoin + curTotal <= amount:
#                 return calculateChange(curTotal + curCoin, curCoins + [curCoin], remaining)
#             else:
#                 return calculateChange(curTotal, curCoins, remaining[1:])
#             #print(curCoin)

#         change = calculateChange(0, [], sorted(coins, reverse=True))
#         return len(change) if type(change) != int else change

class Solution(object):
    # Algorithm: min(dp[i], dp[i - coin])

    def coinChange(self, coins, amount):
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        print(dp)
        print(coins)
        for coin in coins:
            print("DP Before:", dp)
            print(coin)
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], 1 + dp[i - coin])
            print("DP After:", dp)
        return dp[-1] if dp[-1] != MAX else -1




""" TESTS """
S = Solution()

#coins = [1, 2, 5]; amount = 11 ## => 3 coins
#coins, amount = [2], 1
#coins, amount = [1, 5, 10, 25], 100
#coins, amount = [1,2147483647], 2
#coins, amount = [2,5,10,1], 27 ## => 4
# coins, amount = [3,7,405,436], 8839
#coins, amount = [186,419,83,408], 6249
#coins, amount = [176,6,366,357,484,226,1,104,160,331], 5557

res = S.coinChange(coins, amount)
print("--------")
print(res)

### [[419, 419, 419, 419, 419, 419, 419, 419, 408, 408, 408, 408, 186, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83, 83]] 
### VS
### 