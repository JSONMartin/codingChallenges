import re

def is_uppercase(inp): return not re.search('[a-z]', inp)


### TESTING

is_uppercase("c") #== False
is_uppercase("C") #== True
is_uppercase("hello I AM DONALD") #== False
is_uppercase("HELLO I AM DONALD") #== True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") #== False
res = is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") #== True

print(res)