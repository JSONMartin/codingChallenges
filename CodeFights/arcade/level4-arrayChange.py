def arrayChange(inputArray):
    array = inputArray[:]  # Don't modifiy the input data, a la functional programming
    steps = 0

    for i in range(1, len(array)):
        if array[i] <= array[i - 1]:
            adjustedValue = (array[i - 1] + 1)
            steps += abs(adjustedValue - array[i])
            array[i] = adjustedValue

    return steps

# TESTS


# arrayChange([-1000, 0, -2, 0])
arrayChange([1, 1, 1])
