from collections import Counter


def palindromeRearranging(inputString):
    letterCount = Counter(inputString)
    oddPairs = [n for n in letterCount.values() if n % 2 == 1]
    return len(oddPairs) <= 1  # There should be at most 1 odd pairs of letters


""" TESTS """
palindromeRearranging('abbcabb')
