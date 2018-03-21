def circleOfNumbers(circleSize, firstNumber):
    return [n for n in range(circleSize)][firstNumber - (circleSize // 2)]


def circleOfNumbersMathSolution(circleSize, firstNumber):
    return int((firstNumber + circleSize / 2) % circleSize)


""" TESTS """
res = circleOfNumbers(10, 2)
print(res)

res = circleOfNumbersMathSolution(10, 2)
print(res)
