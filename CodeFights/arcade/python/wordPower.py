def wordPower(word):
    num = {ch: abs(ord(ch) - ord('a') + 1) for ch in 'abcdefghijklmnopqrstuvwxyz'}
    return sum([num[ch] for ch in word])
