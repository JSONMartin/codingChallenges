def validate_pin(pin):
    print "Len is:%s" % len(pin)
    if (isinstance(pin, basestring) and pin.isdigit()) and (len(pin) == 4 or len(pin) == 6):
        return True
    else:
        return False

"""
Other solutions
"""
def validate_pin(pin):
    return len(pin) in (4,6) and pin.isdigit()

print validate_pin("111111")
print validate_pin("1111")
print validate_pin("111")