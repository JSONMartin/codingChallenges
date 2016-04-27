def my_parse_int(string):
    return int(filter(str.isdigit, string)) if ( string.strip() == filter(str.isdigit, string) ) else "NaN"

# print my_parse_int("123abc.33")
# print my_parse_int("123")
# print my_parse_int("  1  ")

"""
Other solutions
"""
def my_parse_int(string):
    try:
        return int(string)
    except:
        return 'NaN'

print my_parse_int("123abc.33")
print my_parse_int("123")
print my_parse_int("  1  ")