"""
Just like in the "father" kata, you will have to return the last digit of the nth element in the Fibonacci sequence (starting with 1,1, to be extra clear, not with 0,1 or other numbers).

You will just get much bigger numbers, so good luck bruteforcing your way through it ;)

last_fib_digit(1) == 1
last_fib_digit(2) == 1
last_fib_digit(3) == 2
last_fib_digit(1000) == 5
last_fib_digit(1000000) == 5
"""

def last_fib_digit(n):
    a, b = 1, 1
    aOrB = 'a'

    if n <= 2: return 1

    for i in range(n - 1):
        if aOrB == 'a':
            a = a + b
            aOrB = 'b'
        else:
            b = a + b
            aOrB = 'a'
        #print(a, b)
    
    result = a if aOrB == 'a' else b
    #print(int(str(result)[-1]), result)
    return int(str(result)[-1])


# Also times out
# def last_fib_digit(n):
#     def fibonacci(n):
#         sequence = [1, 1]

#         while len(sequence) <= n - 1:
#             sequence.append(sequence[len(sequence) - 1] + sequence[len(sequence) - 2])
        
#         print(sequence)
#         return sequence[-1]

#     print(fibonacci(n))
#     return int(str(sequence[-1])[-1])

# This solution only works until about 1000....
# import sys
# sys.setrecursionlimit(50000)

# def memoize(fn):
#     memo = {}

#     def memoizer(n):
#         if n not in memo:
#             memo[n] = fn(n)
#         return memo[n]
    
#     return memoizer
    
# def last_fib_digit(n):
#     @memoize
#     def fibonacci(n):
#         if n == 0 or n == 1: return 1
#         return fibonacci(n - 1) + fibonacci(n - 2)
#     print(fibonacci(n))




#last_fib_digit(1) # == 1
#last_fib_digit(2) # == 1
#last_fib_digit(3) # == 2
#res = last_fib_digit(6)
#res = last_fib_digit(1000) # == 2
#last_fib_digit(1000) # == 5
res = last_fib_digit(21) # == 6
#res = last_fib_digit(1000000) # == 5

print(res)