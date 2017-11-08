"""
The vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2.
Given a lowercase string that has alphabetic characters only and no spaces, return the length of the longest vowel substring.

Good luck!
"""

"codewars"

def solveImprovedSolution(string):
    return max(map(len, ''.join(char if char in 'aeiou' else ' ' for char in string).split()))

def solve(string):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    substrings = []

    for idx, char in enumerate(string):
        print(char, idx)
        if char in vowels:
            vowelCheckIdx = idx
            while vowelCheckIdx < len(string) and string[vowelCheckIdx] in vowels:
                vowelCheckIdx += 1
            substrings += [string[idx:vowelCheckIdx]]
            idx = vowelCheckIdx = 1

    return max([len(substr) for substr in substrings])


res = solve("codewarriors")
improvedSolutionRes = solveImprovedSolution("codewarriors")
print("Result:", improvedSolutionRes, " = ", res, improvedSolutionRes == res)