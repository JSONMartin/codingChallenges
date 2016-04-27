def xo(s):
    s = s.lower()
    x_counter = 0
    o_counter = 0
    for letter in s:
        if letter == 'x':
            x_counter+=1
        if letter == 'o':
            o_counter+=1
    if x_counter == o_counter:
        return True
    else:
        return False

def vampire_test(x, y):
    if x < 0 and y < 0: return False
    total = str(x*y)
    fangs = str(x) + str(y)
    for digit in total:
        if digit in fangs:
            fangs = fangs.replace(digit, '', 1)

    print fangs

    if len(fangs) == 0: return True
    else: return False

