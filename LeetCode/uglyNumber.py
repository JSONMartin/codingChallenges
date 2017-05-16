# """Write a program to check whether a given number is an ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

# Note that 1 is typically treated as an ugly number."""
# def findPrimes(numToFind):
#     def findPrime(n):
#         for j in range(3, n//2, 2):
#             print("j:", j)
#             if (n / j) % 1 != 0: return False
#         return True

#     primes = []
#     for i in range(3, numToFind // 2, 2):
#         print("i:", i)
#         if findPrime(i): primes.append(i)
#     print(primes)


# def isPrime(n):
#     for i in range(2, n//2 + 1):
#         if (n/i) % 1 == 0: return False
#     return True

# def findPrimes(n):
#     primes = []
#     for i in range(7, n//2):
#         if isPrime(i): primes.append(i)
#     return primes

class Solution(object):
    def isUgly(self, num):
        if num <= 0: return False
        if num == 1: return True
        for divisor in [2, 3, 5]:
            # if (num / i) % 1 == 0: return True
            while num and num % divisor == 0:
                num /= divisor
        return num == 1
        
        # primes = findPrimes(num)
        # for p in primes:
        #     if (num/p) % 1 == 0: return False
        # return True


# findPrimes(1000)
res = Solution().isUgly(2147483649)
print(res)










# def isPrime(n):
#     for i in range(2, n//2 + 1):
#         if (n/i) % 1 == 0: return False
#     return True

# def findPrimes(n):
#     primes = []
#     for i in range(7, n):
#         if isPrime(i): primes.append(i)
#     return primes


#res = isPrime(9)
# res = findPrimes(100)
# print(res)