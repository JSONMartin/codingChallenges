# https://www.codewars.com/kata/5287e858c6b5a9678200083c/solutions/python

def narcissistic( value ):
    value_string = str(value)
    num_digits = len(value_string)
    new_digit = 0

    for digit in value_string:
        new_digit += int(int(digit) ** num_digits)

    return value == int(new_digit)
