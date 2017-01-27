# https://www.codewars.com/kata/54a2e93b22d236498400134b/train/python
"""
Prior to having fancy iPhones, teenagers would wear out their thumbs sending SMS messages on candybar-shaped feature phones with 3x4 numeric keypads.

------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|     | |space| |     |
|  *  | |  0  | |  #  |
------- ------- -------
Prior to the development of T9 (predictive text entry) systems, the method to type words was called "multi-tap" and involved pressing a button repeatedly to cycle through the possible values.

For example, to type a letter "R" you would press the 7 key three times (as the screen display for the current character cycles through P->Q->R->S->7). A character is "locked in" once the user presses a different key or pauses for a short period of time (thus, no extra button presses are required beyond what is needed for each letter individually). The zero key handles spaces, with one press of the key producing a space and two presses producing a zero.

In order to send the message "WHERE DO U WANT 2 MEET L8R" a teen would have to actually do 47 button presses. No wonder they abbreviated.

For this assignment, write a module that can calculate the amount of button presses required for any phrase. Punctuation can be ignored for this exercise. Likewise, you can assume the phone doesn't distinguish between upper/lowercase characters (but you should allow your module to accept input in either for convenience).

Hint: While it wouldn't take too long to hard code the amount of keypresses for all 26 letters by hand, try to avoid doing so! (Imagine you work at a phone manufacturer who might be testing out different keyboard layouts, and you want to be able to test new ones rapidly.)
"""
def presses(phrase):
    groupings = {
        1: ['1'],
        2: ['A', 'B', 'C', '2'],
        3: ['D', 'E', 'F', '3'],
        4: ['G', 'H', 'I', '4'],
        5: ['J', 'K', 'L', '5'],
        6: ['M', 'N', 'O', '6'],
        7: ['P', 'Q', 'R', 'S', '7'],
        8: ['T', 'U', 'V', '8'],
        9: ['W', 'X', 'Y', 'Z', '9'],
        0: [' ', '0'],
        '#': ['#'],
        '*': ['*']

    }
    mapping = {
        'A': 2,
        'B': 2,
        'C': 2,
        'D': 3,
        'E': 3,
        'F': 3,
        'G': 4,
        'H': 4,
        'I': 4,
        'J': 5,
        'K': 5,
        'L': 5,
        'M': 6,
        'N': 6,
        'O': 6,
        'P': 7,
        'Q': 7,
        'R': 7,
        'S': 7,
        'T': 8,
        'U': 8,
        'V': 8,
        'W': 9,
        'X': 9,
        'Y': 9,
        'Z': 9,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '0': 0,
        ' ': 0,
        '1': 1,
        '*': '*',
        '#': '#'
    }

    keypress_count = 0

    for char in phrase.upper():
        group, i = groupings[mapping[char]], 0

        while i < len(group):
            if group[i] == char:
                break
            i += 1

        keypress_count += i + 1

    return keypress_count


### TESTS
"""
Test.assert_equals(presses("LOL"), 9)
Test.assert_equals(presses("HOW R U"), 13)
"""
res = presses('#')
print(res)
