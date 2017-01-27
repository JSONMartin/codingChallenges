def filter_string(string):
    return int(''.join(list(filter(lambda x: x.isdigit(), string))))
    #return int(''.join([x for x in string if x.isdigit()]))


print( filter_string("a12bc3") )