def lineEncoding(s):
    idx = 0
    length = len(s)
    curLetter, letterCounter = s[0], 0
    encodedStr = ""

    while idx < length:
        if s[idx] == curLetter:
            letterCounter += 1
        else:
            encodedStr += str(letterCounter) + curLetter if letterCounter > 1 else curLetter
            curLetter, letterCounter = s[idx], 1
        idx += 1

    encodedStr += str(letterCounter) + curLetter if letterCounter > 1 else curLetter
    print(encodedStr)
    return encodedStr


lineEncoding('aabbbc')
