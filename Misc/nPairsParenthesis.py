"""
* 0 -> []
* 1 -> ['()']
* 2 -> ['(())', '()()']
* 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
"""

class Parentheses(object):
    def find_pair(self, num_pairs):
        if num_pairs == None: raise TypeError
        if num_pairs < 0: raise ValueError
        if num_pairs == 0: return []

        result = []

        def generatePairs(current = '', leftRemaining = num_pairs, rightRemaining = num_pairs):
            # Base Case
            if leftRemaining == 0 and rightRemaining == 0:
                result.append(current)
                return

            if leftRemaining > 0:
                generatePairs(current + "(", leftRemaining - 1, rightRemaining)
            if rightRemaining > leftRemaining:
                generatePairs(current + ")", leftRemaining, rightRemaining - 1)

        generatePairs()
        return result

### TESTS ###
Parentheses().find_pair(3)