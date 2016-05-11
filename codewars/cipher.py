# Source: http://www.codewars.com/kata/546937989c0b6ab3c5000183/train/python

def encryptor(key, message):
    def shift(c, key):
        if c == c.upper():
            return ((ord(c) + key - ord('A')) % 26) + ord('A')
        elif c == c.lower():
            return ((ord(c) + key - ord('a')) % 26) + ord('a')
    result = ''
    for char in message:
        if char.isalpha(): result+=chr(shift(char, key))
        else: result+=char
    return result

#print(encryptor(13, ''))
#print(encryptor(13, 'Caesar Cipher'))
print(encryptor(-5, 'Hello World!'))
#print(encryptor(27, 'Whoopi Goldberg'))