# https://www.codewars.com/kata/memoized-fibonacci/train/python

# Self contained Memoized

# def fibonacci(n):
#     memo = {}
#
#     def fiboCalc(n):
#         if n in memo: return memo[n]
#         if n in [0, 1]:
#             return n
#
#         memo[n] = fiboCalc(n - 1) + fiboCalc(n - 2)
#         return memo[n]
#
#     return fiboCalc(n)

# Decorator solution

def memoized(fn):
    cache = {}

    def wrappedFn(arg):
        if arg in cache:
            return cache[arg]

        cache[arg] = fn(arg)
        return cache[arg]

    return wrappedFn

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
