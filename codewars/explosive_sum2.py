# def exp_sum(n):
#     count = 0
#     memo = {}
#     results = []
#     available = [i for i in range(1, n + 1)]
#
#     def calc_sum(total, soFar, index):
#         if total <= 0:
#             results.append(soFar)
#             return
#         if index >= len(available):
#             return
#
#         amountWithCoin = 0
#
#         while amountWithCoin <= total:
#             remaining = total - amountWithCoin
#             calc_sum(remaining, soFar, index + 1)
#             amountWithCoin += available[index]
#             soFar += [available[index]]
#
#         print(results)
#
#     calc_sum(n, [], 0)
#
#     return count

CALL_COUNT = 0

def exp_sum(n):
    coins = [i for i in range(1, n + 1)]
    memo = {}

    def find_sum(coins, money, index):
        global CALL_COUNT
        CALL_COUNT += 1

        KEY = str(money) + "-" + str(index)
        if KEY in memo: return memo[KEY]

        elif money == 0: return 1
        elif index >= len(coins): return 0

        amountWithCoin = 0
        ways = 0

        while amountWithCoin <= money:
            remaining = money - amountWithCoin
            ways += find_sum(coins, remaining, index + 1)
            amountWithCoin += coins[index]


        #return ways
        memo[KEY] = ways
        return memo[KEY]

    return find_sum(coins, n, 0)






### TESTS
res = exp_sum(5) # 2 -> 1+1 , 2
print(res)
# #print(sorted(res))

print(CALL_COUNT)
