def primes_sieve(limit):
    limitn = limit + 1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i * 2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    #return primes, not_prime
    return not_prime


#print(primes_sieve(100000))
def smallest(n):
    sieve = list(primes_sieve(999999))
    sieve.reverse()
    numberToTry = n

    while len(sieve) > 0:
        found = True
        curAttempt = sieve.pop()
        if curAttempt < n: continue
        
        for i in range(1, n+1):
            #print("CurAttempt:%d | i:%d" % (curAttempt, i))
            if curAttempt % i != 0:
                found = False
                break
        
        if found: return curAttempt


    # found = False
    # while not found:
    #     found = True
    #     if numberToTry not in sieve:
    #         found = False
    #         numberToTry += 1
    #         continue
        
    #     for i in range(1, n+1):
    #         if numberToTry % i != 0:
    #             numberToTry+= 1
    #             found = False
    #             break
    #     if found: return numberToTry
    # return numberToTry

res = smallest(40)
print(res)
