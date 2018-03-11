def arrayMaximalAdjacentDifference(inputArray):
    return max([max((abs(inputArray[x] - inputArray[x - 1]), abs(inputArray[x + 1] - inputArray[x]))) for x in range(1, len(inputArray) - 1)])


""" TESTS """
inputArray = [-1, 4, 10, 3, -2]
arrayMaximalAdjacentDifference(inputArray)
