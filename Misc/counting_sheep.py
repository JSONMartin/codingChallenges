count_sheeps = lambda arrayOfSheeps: len([s for s in arrayOfSheeps if s == True])

# or

count_sheeps = lambda arrayOfSheeps: arrayOfSheeps.count(True)

### TESTING

array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True]

res = count_sheeps(array1)
print(res)