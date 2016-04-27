def vowel_indices(word):
    positions = []

    for x in xrange(len(word)):
        if word[x].upper() in ['A','E','I','O','U']:
            positions.append(x)

    return positions

print vowel_indices('tower')