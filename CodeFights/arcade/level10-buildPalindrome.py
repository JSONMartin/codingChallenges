"""
Given a string, find the shortest possible string which can be achieved by adding characters to the end of initial string to make it a palindrome.

Example

For st = "abcdc", the output should be
buildPalindrome(st) = "abcdcba".
"""


def checkPalindrome(inputString):
    if len(inputString) <= 1:
        return True

    return inputString[0] == inputString[-1] and checkPalindrome(inputString[1:-1])


def buildPalindrome(str):
    # Starting at the end of the string, check backwards to find if there are any palindromes
    for idx in range(len(str) - 1):
        substr = str[idx:len(str)]
        if checkPalindrome(substr):
            return str + str[:str.index(substr)][::-1]

    return str + str[:(len(str) - 1)][::-1]


res = buildPalindrome("abaa")
print(res)
