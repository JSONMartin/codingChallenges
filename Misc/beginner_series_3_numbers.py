## https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

# Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.
#
# Note! a and b are not ordered!
#
# Example:
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

def get_sum(a, b):
    return sum([i for i in range(min(a,b), max(a,b) + 1)])

def get_sum_og(a,b):
    if a == b: return a

    total = 0

    for i in range(min(a,b), max(a,b) + 1):
        total+= i

    return total

###############
### TESTING
###############
res = get_sum(1, 1)
print(res)