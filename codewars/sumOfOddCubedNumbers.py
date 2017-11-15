# https://www.codewars.com/kata/580dda86c40fa6c45f00028a/train/python
"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
This function will return undefined (NULL in PHP) if any of the values aren't numbers.
"""

def cube_odd(arr):
    try:
        return sum(filter(lambda x: x % 2 == 1, [i ** 3 for i in arr]))
    except:
        return None

### TESTS ###
result = cube_odd([1, 2, 3, 4])
print(result)