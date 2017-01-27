## https://www.codewars.com/kata/525f039017c7cd0e1a000a26/train/python

# Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.
#
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.
#
# If the input number is already a palindrome, the number of steps is 0.
#
# Input will always be a positive integer.
#
# For example, start with 87:
#
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
#
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

# Estimated time: 15 min
# Actual time: 4 min

def palindrome_chain_length(n):
    is_palindrome = lambda s: str(s) == str(s)[::-1]

    current, counter = n, 0

    while True:
        if is_palindrome(current):
            return counter
        else:
            current = current + int(str(current)[::-1])
            counter += 1

res = palindrome_chain_length(87)
print(res)


## Another solution
def palindrome_chain_length(n):
    counter = 0

    while str(n) != str(n)[::-1]:
        n = n + int(str(n)[::-1])
        counter += 1

    return counter

