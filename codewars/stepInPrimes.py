import math

def isPrime(n):
    if n % 2 == 0: return False
    for i in range(2, math.sqrt(n)):
        if n % i == 0: return False
    return True

def step(g, m, n):
    primes = []
    for i in range(m, n + 1):
        if isPrime(i): primes.append(i)
    print(primes)

    results = None
    for i in range(0, len(primes) - 1):
        # if primes[i] - primes[i - 1] == g:
        #     results = [primes[i - 1], primes[i]]
        #     break
        # idx = primes.index(primes[i] + g) if primes[i] + g in
        # [].index
        #print("Idx:", idx)
        if primes[i] + g in primes:
            results = [primes[i], primes[i] + g]
            break

    return results


###
res = step(2,100,110) #=> [101, 103]
print("RES:", res)