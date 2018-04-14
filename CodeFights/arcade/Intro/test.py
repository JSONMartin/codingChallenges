def checkPalindrome(inputString):
    print(inputString, list(inputString))
    stringArray = list(inputString)

    while len(stringArray) > 1:
        if stringArray.pop(0) != stringArray.pop():
            return False

    return True


res = checkPalindrome("racecara")
print(res)
