## Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

## The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution(object):
    def isValid(self, s):
        brackets = []

        for ch in s:
            if ch in '([{': # instead of... #if ch in ['(', '{', '[']:
                brackets.append(ch)
            elif ch in ')}]': # instead of ... #elif ch in [')', '}', ']']:
                if len(brackets) <= 0 or brackets[-1] != ch.replace(')', '(').replace('}', '{').replace(']', '['):
                    return False
                else:
                    brackets.pop()

        return True if len(brackets) == 0 else False

#########
# TESTS #
#########

# Push each opening bracket into a stack
# If closing bracket
    # Pop each closing bracket off the stack and compare with current char

# () count — 1
# {} count - 0
# [] count - 2
# last_bracket - [

# ([]) - Valid
# ([[])) - Invalid

s = Solution()
res = s.isValid("((([])))")
#res = s.isValid("([[]))")
print("---------------------")
print(res)