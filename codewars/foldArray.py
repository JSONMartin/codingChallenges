def fold_array(array, runs):
    array = array[:]

    while runs > 0:
        middle = len(array) // 2

        i = 0
        while i < middle:
            array[i] += array.pop()
            i += 1

        runs -= 1

    return array

res = fold_array([1, 2, 3, 4, 5], 2)
print(res)