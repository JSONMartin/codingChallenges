#Source: http://www.codewars.com/kata/5541f58a944b85ce6d00006a
def productFib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b # This is actually a Tuple assignment
    return [a, b, a * b == prod]

def productFibMemoized(prod): # Memoized solution
    fibbed = { 0: 0, 1: 1}
    def fib(n):
        if n in fibbed:
            return fibbed[n]
        else:
            fibbed[n] = fibbed[n-1] + fibbed[n-2]
            return fibbed[n]
        #if n == 1 or n == 2: return 1
        #else: return fib(n-1) + fib(n-2)
    done = False
    count = 0
    while not done:
        count += 1
        result = fib(count) * fib(count + 1)
        if result > prod: return [fib(count), fib(count + 1), False]
        elif result == prod: return [fib(count), fib(count + 1), True]
    return False

print(productFib(800))