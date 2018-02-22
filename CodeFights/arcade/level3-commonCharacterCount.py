from collections import Counter


def commonCharacterCount(s1, s2):
    s1Count, s2Count = Counter(s1), Counter(s2)

    if len(s1) >= len(s2):
        difference = s1Count - s2Count
        s1Count.subtract(difference)
        return sum(s1Count.values())
    else:
        difference = s2Count - s1Count
        s2Count.subtract(difference)
        return sum(s2Count.values())


# TESTS
s1 = "aabcc"
s2 = "adcaa"
commonCharacterCount(s1, s2)
