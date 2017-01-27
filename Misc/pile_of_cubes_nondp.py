# Works with Recursion, but maxes out with time because of depth
import sys
sys.setrecursionlimit(100000)

def find_nb(total):
    def build(row_n, current_total = 0):
        #print("Current Total:%d, Row_n:%d" % (current_total, row_n))
        if row_n == 1:
            return current_total + (row_n ** 3)
        else:
            return build(row_n - 1, current_total + (row_n**3))

    current_total, i = 0, 0

    while current_total < total:
        i += 1
        #print("Trying #:%d" % i)
        current_total = build(i)

    return i if (current_total == total) else -1
### TESTS

# res = find_nb(1071225) #--> 45
#res = find_nb(91716553919377) #--> -1
#res = find_nb(4183059834009) #--> 2022
#res = find_nb(4183059834009) #--> 2022
res = find_nb(418304459834009) #--> -1
#res = find_nb(1025292944081385001) #--> 45001

print(res)