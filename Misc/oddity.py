# Math solution
def oddity(n):
    return 'odd' if n**0.5 == int(n**0.5) else 'even'

# Iterative solution
def oddity(n):
    print(n)
    if n == 1: return 'odd'
    divisors = []
    counter = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            divisors.append(i)
            counter+=1
    divisors.append(n)

    print(divisors)
    return 'even' if (len(divisors) == 0 or len(divisors) % 2 == 0) else 'odd'
    #return 'even' if (counter == 0 or counter % 2 == 0) else 'odd'
