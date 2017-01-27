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
#
#
# import copy
#
# class Solution(object):
#     def generateParenthesis(self, n):
#         results = []
#         str_results = []
#         current = [[] for x in range(n)]
#         start = [[[[]]]]
#
#         # def generateCombos(remaining):
#         #     print("Remaining:")
#         #     print(remaining)
#         #     results.append(copy.deepcopy(remaining))
#         #     el = remaining.pop(0)[:]
#         #     for i in range(len(remaining)):
#         #         print("Remaining:")
#         #         print(remaining)
#         #         remaining[i].append(el)
#         #         results.append(copy.deepcopy(remaining))
#         #         generateCombos(remaining[0])
#         #         remaining[i].pop()
#         #
#         #     #results.append(el.append(copy.deepcopy(remaining)))
#         #     el.append(copy.deepcopy(remaining))
#         #     results.append(el)
#         #     # while len(remaining) > 0:
#
#         def generateAllCombos(start):
#             results.append(start)
#             pos = start[0]
#             history = [pos]
#             #print("Pos:" + str(pos))
#             #print("History:" + str(history))
#
#             while pos:
#                 #printCombo(pos)
#                 history.append(pos[:])
#                 pos = pos[0]
#                 #print("Pos:" + str(pos))
#                 #print("History:" + str(history))
#
#             last = history.pop()
#             while history:
#                 current = history.pop()
#                 print("current:" + str(current))
#                 print("Last:" + str(last))
#                 print("History:" + str(history))
#                 #print(str((current + last)))
#                 results.append(current + last)
#                 results.append(last + current)
#                 last = current
#                 # for item in h:
#                 #     print(item)
#
#
#         def printCombo(p):
#             str_result = ""
#             #print(results)
#             s = str(p)
#             res = s[1:len(s)-1].replace(",", "").replace(" ", "").replace("[", "(").replace("]", ")")
#             print(res)
#             return res
#
#
#         def printCombos():
#             nonlocal results
#             nonlocal str_results
#             #print(results)
#             for i in results:
#                 s = str(i)
#                 res = s[1:len(s)-1].replace(",", "").replace(" ", "").replace("[", "(").replace("]", ")")
#                 print(res)
#                 str_results.append(res)
#
#                 #s = i[1:len(i)]
#                 #s = str(i)[1:len(i)]
#                 #print(s)
#
#
#         #results.append(0)
#         #generateCombos(current[:])
#         generateAllCombos(start)
#         #results.append(0)
#         print("Results:")
#         print(results)
#         printCombos()
#         print(str_results)

class Solution(object):
    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)




#########
# TESTING
#########
s = Solution()
res = s.generateParenthesis(3)
print(res)