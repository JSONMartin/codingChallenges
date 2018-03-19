def alphabeticShift(inputStr):
    shifted = ""

    for char in inputStr:
        startChar = 'a' if char.islower() else 'A'
        newChar = chr(ord(startChar) + ((ord(char) + 1 - ord(startChar)) % 26))
        shifted += newChar

    return shifted


""" TESTS """
res = alphabeticShift("crazy")
print(res)
