# https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python
"""
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""

# Read num from right to left.
# When hit a non-zero number, add 0s for tens digit place
def expanded_form(num):
    n = str(num)

    i, counter, parts = len(n) - 1, 0, []

    while i >= 0:
        if int(n[i]) > 0:
            parts += [n[i] + "0" * counter]
        counter += 1
        i -= 1

    return ' + '.join(reversed(parts))

### TESTS ###
#from Test.Test import Test
#test = Test
expanded_form(12) # => , '10 + 2'
expanded_form(42) # => , '40 + 2'
expanded_form(70304) # => , '70000 + 300 + 4'