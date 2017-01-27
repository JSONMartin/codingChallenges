# # Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# #
# # For example, given n = 3, a solution set is:
# #
# # [
# #   "((()))",
# #   "(()())",
# #   "(())()",
# #   "()(())",
# #   "()()()"
# # ]


# My solution, faster by 10 ms
class Solution(object):
    def generateParenthesis(self, n):
        combos = []

        def generateCombo(current, l_parens_remaining, r_parens_remaining, combos):
            if l_parens_remaining <= 0 and r_parens_remaining <= 0:
                combos.append(current)
            else:
                if l_parens_remaining > 0:
                    generateCombo(current + "(", l_parens_remaining - 1, r_parens_remaining, combos)
                if r_parens_remaining > l_parens_remaining and r_parens_remaining > 0:
                    generateCombo(current + ")", l_parens_remaining, r_parens_remaining - 1, combos)


        generateCombo("", n, n, combos)
        return combos

# Other solution, slower by 10 ms. But more elegant code?

# class Solution2(object):
#     def generateParenthesis(self, n):
#         def generateCombo(current, l_parens_remaining, r_parens_remaining, combos=[]):
#             if l_parens_remaining:
#                 generateCombo(current + "(", l_parens_remaining - 1, r_parens_remaining)
#             if r_parens_remaining > l_parens_remaining:
#                 generateCombo(current + ")", l_parens_remaining, r_parens_remaining - 1)
#             if not r_parens_remaining:
#                 combos.append(current)
#             return combos
#
#         return generateCombo("", n, n)


#########
# TESTING
#########
s = Solution()
res = s.generateParenthesis(3)
print(res)