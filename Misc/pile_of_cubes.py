def find_nb(total):
    calculated = {1: 1}

    def build(row_n, current_total = 0):
        if row_n in calculated: return calculated[row_n] + current_total
        else: return build(row_n - 1, current_total + (row_n**3))

    current_total, i = 0, 0

    while current_total < total:
        i += 1
        current_total = build(i)
        calculated[i] = current_total

    return i if (current_total == total) else -1

############
### TESTS
############
#res = find_nb(1071225) #--> 45
#res = find_nb(91716553919377) #--> -1
#res = find_nb(4183059834009) #--> 2022
#res = find_nb(1025292944081385001) #--> 45001
res = find_nb(418304459834009) #--> -1

print(res)