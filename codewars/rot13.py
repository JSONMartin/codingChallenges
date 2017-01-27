import re
import string

def rot13(message):
    result, ROT = "", 13

    for ch in message:
        if not re.match('[a-zA-Z]', ch):
            result += ch
            continue
        z = 'Z' if ch == ch.upper() else 'z'
        a = 'A' if ch == ch.upper() else 'a'
        print(ord(ch))
        if (ord(ch) + ROT) <= ord(z):
            result += chr(ord(ch) + ROT)
        else:
            result += chr(ord(a) + (ord(ch) - ord(a) + 13) % 13)

    print(result)
    return result



### TESTING
rot13(' ')
