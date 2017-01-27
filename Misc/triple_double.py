
# Refind way:
def triple_double(n1, n2):
    return any(i*3 in str(n1) and i*2 in str(n2) for i in '0123456789')

def origional_triple_double(num1, num2):
    #n1, n2 = collections.Counter(str(num1)), collections.Counter(str(num2))
    n1, n2 = str(num1), str(num2)

    n1_matches, n2_matches = {}, {}

    def find_match(num_str, matches, threshold):
        last = num_str[0]
        counter = 1

        for n in range(1, len(num_str)):
            if last == num_str[n]:
                counter += 1
                if counter >= threshold:
                    matches[last] = counter
            else:
                last = num_str[n]
                counter = 1

    find_match(n1, n1_matches, 3)
    find_match(n2, n2_matches, 2)

    #print(n1_matches)
    #print(n2_matches)

    for i in n1_matches:
        if n1_matches[i] == 3 and i in n2_matches and n2_matches[i] == 2:
            return 1

    return 0

res = triple_double(451999277, 41177722899)
print(res)