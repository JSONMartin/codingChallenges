"""
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1, 4, 9, 36, 49, 196, 441, 1764.
The sum of the squared divisors is 2500 which is 50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and n whose sum of squared divisors is itself a square.
42 is such a number.

The result will be an array of arrays(in C an array of Pair), each subarray having two elements,
first the number whose squared divisors is a square and then the sum of the squared divisors.

Examples:

list_squared(1, 250) --> [[1, 1], [42, 2500], [246, 84100]]
list_squared(42, 250) --> [[42, 2500], [246, 84100]]
The form of the examples may change according to the language, see Example Tests: for more details.
"""
import math

def list_squared(start, end):
    results = []

    for n in range(start, end):
        # Find divisors for each number
        squared_sum = 0

        for i in range(1, math.floor(math.sqrt(n)) + 1):
            if n % i == 0:
                if n / i == i: squared_sum += (i ** 2)
                else: squared_sum += (i ** 2) + ((n//i) ** 2)

        if math.sqrt(squared_sum) % 2 == 0: results.append([n, squared_sum])

    return [[1, 1]] + results if start <= 1 else results


res = list_squared(1, 250)
print(res)


