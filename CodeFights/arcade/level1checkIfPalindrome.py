# Simple solution
# checkPalindrome = lambda inputString: inputString == inputString[::-1]

# Iterative Solution


def checkPalindromeIterative(inputString):
    idx = 0
    mid = len(inputString) // 2

    while idx != mid:
        if inputString[idx] != inputString[-(idx + 1)]:
            return False
        idx += 1

    return True

# Recursive solution


def checkPalindromeRecursive(inputString):
    if len(inputString) <= 1:
        return True

    return inputString[0] == inputString[-1] and checkPalindrome(inputString[1:-1])


# Tests
tests = [('radar', True), ('lala', False), ('racecar', True)]

for testStr, expectedResult in tests:
    res = checkPalindromeIterative(testStr)
    print(f"testStr:{testStr} | expectedresult:{expectedResult} | actualResult:{res}")
