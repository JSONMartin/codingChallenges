# You have to create a function that takes a positive integer number and returns the next bigger number formed by the same digits:
#
# next_bigger(12)==21
# next_bigger(513)==531
# next_bigger(2017)==2071
# If no bigger number can be composed using those digits, return -1:
#
# next_bigger(9)==-1
# next_bigger(111)==-1
# next_bigger(531)==-1

##1234567890 => 1234567908

# 59884848498535 => 59884848483559

def next_bigger(n):
    n_list = list(str(n))
    l, r = None, None

    try:
        for i in range(len(n_list) - 2, -1, -1):
            print(n_list[i])
            combination = n_list[:]
            combination.append(combination.pop(i))
            combination_str = "".join(combination)
            combo = int(combination_str)
            print(combination_str)
            if combo > n:
                l = combo
                break

        for i in range(1, len(n_list)):
            print(n_list[i])
            combination = n_list[:]
            combination.insert(0, combination.pop(i))
            combination_str = "".join(combination)
            combo = int(combination_str)
            print(combination_str)
            if combo > n:
                r = combo
                break

        if r == l and l == None:
            return -1
        elif r == None:
            return l
        elif l == None:
            return r
        else:
            return min(l, r)
    except:
        return -1

    return -1




def next_bigger_other(n, idx = 0):
    def generate_next_attempt(n, idx, direction):
        n_str = str(n)
        n_list = list(n_str)

        if direction == 'l_to_r':
            a_idx, b_idx = idx + 0, idx + 1
        else:
            a_idx, b_idx = idx - 1, idx - 2

        try:
            n_list[a_idx], n_list[b_idx] = n_list[b_idx], n_list[a_idx]
        except:
            return -1

        n_str = "".join(n_list)
        attempt = n_str
        print(n_str)
        if idx == len(str(n)):
            return -1
        if int(attempt) > n:
            return int(attempt)
        else:
            return generate_next_attempt(int(attempt), idx + 1, direction)

    n_str = str(n)
    start = min(n_str)
    start_idx = n_str.index(start)

    l_to_r = generate_next_attempt(n, 0, 'l_to_r')
    r_to_l = generate_next_attempt(n, 0, 'r_to_l')

    candidates = []
    if l_to_r > n:
        candidates.append(l_to_r)
    if r_to_l > n:
        candidates.append(r_to_l)

    print("LtoR: %d | RtoL: %d" % (l_to_r, r_to_l))
    print("Winner:%d" % min(candidates))
    return min(candidates)













# Calc all possible solutions and find in sorted array
def next_bigger_OG(n):
    if n < 10: return -1

    def all_possibilities(cur, remaining, possible):
        # Base Case
        if len(remaining) <= 0:
            possible.append(int(cur))

        for i in range(len(remaining)):
            r = remaining[i]
            all_possibilities(cur + r, remaining[0:i] + remaining[i+1:], possible)

    # Generate all possible combinations and sort for easier searching
    results = []
    all_possibilities("", str(n), results)
    results = list(set(results))
    results.sort()

    # Search for next higher number, if exists
    idx = results.index(n)
    if idx < len(results) - 1:
        return results[idx+1]
    else:
        return -1



###########
### TESTING
###########

# next_bigger(12)==21
# next_bigger(513)==531
#res = next_bigger(2017)

#res = next_bigger(1234567890)
#res = next_bigger(144)

#res = next_bigger(513)

res = next_bigger(9876543210)
print("----------------")
print(res)