import re

def is_digit(n):
    return True if len(n) == 1 and re.match("^-?[0-9]+$", n) != None else False


print( is_digit(" ") )
print( is_digit("7") )
