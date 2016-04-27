def solution(number):
    total = 0
    for i in xrange(number):
        if (i % 3 == 0 or i % 5 == 0):
            total += i
    return total

print solution(1)
print solution(3)
print solution(10)