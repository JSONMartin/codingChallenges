# https://www.codewars.com/kata/catching-car-mileage-numbers/train/python

def is_interesting(number, awesome_phrases, check_adjacent = True):
    number_str = str(number)

    if number == 98 or number == 99: return 1
    if len(number_str) < 3 or number < 99: return 0

    # Check if all digits followed by zeroes
    if number_str[1:] == "0" * (len(number_str) - 1): return 2

    # Check if every digit is the same number
    if all(map(lambda x: x == number_str[0], number_str)): return 2

    # Check if is sequential
    is_sequential, i, n = True, 1, int(number_str[0])

    while is_sequential and i < len(number_str):
        if int(number_str[i]) == 0 and int(number_str[i - 1]) == 9:
            n = 0
            i += 1
        elif int(number_str[i]) != n + i:
            is_sequential = False
        else:
            i += 1

    if is_sequential == True:
        return 2

    is_sequential, i, n = True, 1, int(number_str[0])

    while is_sequential and i < len(number_str):
        if int(number_str[i]) == 0 and int(number_str[i - 1]) == 1:
            n = 0
            i += 1
        elif int(number_str[i]) != n - i:
            is_sequential = False
        else:
            i += 1

    if is_sequential == True:
        return 2

    # Check if palindrome
    if number_str == number_str[::-1]: return 2

    # Check if matches awesome_phrases array
    if number in awesome_phrases: return 2

    if check_adjacent and ( is_interesting(number + 1, awesome_phrases, False) == 2 or is_interesting(number + 2, awesome_phrases, False) == 2):
        return 1
    else:
        return 0


# Check if all digits followed by zeroes
#res = is_interesting(1000, [])
#print(res)

# Check if every digit is the same number
#res = is_interesting(1234, [])
#print(res)

# Check if is sequential
#res = is_interesting(1234, [])
#res = is_interesting(4321, [])
#print(res)

# Check if palindrome
# res = is_interesting(1221, [])
# print(res)

# Check if matches awesome_phrases
# res = is_interesting(35675, [22, 35678])
# print(res)


#print(is_interesting(3, [1337, 256])) # Expected 0
#print(is_interesting(1336, [1337, 256])) # Expected 1
#print(is_interesting(1337, [1337, 256])) # Expected 2

#print(is_interesting(11208, [1337, 256])) # Expected 0

#print(is_interesting(11209, [1337, 256])) # Expected 1
#print(is_interesting(11211, [1337, 256])) # Expected 2
#print(is_interesting(67890, [1337, 256])) # Expected 2

#print(is_interesting(3210, [1337, 256])) # Expected 2
#print(is_interesting(654, [1337, 256])) # Expected 2

#print(is_interesting(110, [1337, 256])) # Expected 1





# test.describe("Basic inputs")
# test.it("should work, dangit!")
# tests = [
# 	{'n': 3, 'interesting': [1337, 256], 'expected': 0},
# 	{'n': 1336, 'interesting': [1337, 256], 'expected': 1},
# 	{'n': 1337, 'interesting': [1337, 256], 'expected': 2},
# 	{'n': 11208, 'interesting': [1337, 256], 'expected': 0},
# 	{'n': 11209, 'interesting': [1337, 256], 'expected': 1},
# 	{'n': 11211, 'interesting': [1337, 256], 'expected': 2},
# ]
# for t in tests:
# 	test.assert_equals(is_interesting(t['n'], t['interesting']), t['expected'])