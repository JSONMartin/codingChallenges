# Improved Solution
def rgb(r, g, b):
    check_range = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b)) # Python 3 syntax
    #return ("%02X%02X%02X") % (check_range(r), check_range(g), check_range(b)) # Python 2 syntax

# Original Solution
# def rgb(r, g, b):
#     def check_range(num): # Ensures number is between 0-255
#         if(num <= 0): return 0
#         elif(num >= 255): return 255
#         else: return num
#
#     return str.upper(hex(check_range(r))[2:]).zfill(2) + str.upper(hex(check_range(g))[2:]).zfill(2) + str.upper(hex(check_range(b))[2:]).zfill(2)

'''
TESTS
'''
print(rgb(1, 1, 1))