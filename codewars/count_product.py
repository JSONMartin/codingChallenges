# Description:
#
# Count the number of exclamation marks and question marks, return the product.
# Examples
#
# Product("") == 0
# product("!") == 0
# Product("!ab? ?") == 2
# Product("!!") == 0
# Product("!??") == 2
# Product("!???") == 3
# Product("!!!??") == 6
# Product("!!!???") == 9
# Product("!???!!") == 9
# Product("!????!!!?") == 20
import re

def Product(str):
    exclamation_count, question_count = 0, 0

    for ch in str:
        if ch == '!': exclamation_count += 1
        elif ch == '?': question_count += 1

    return exclamation_count * question_count

### TESTS

Product("!!!???") == 9