# def reverse(str, res = ""):
#     length = len(str)
#     if length == 1: return res + str
#     else: return reverse(str[:length - 1], res + str[length - 1])
#
# res = reverse("hello world!")
# print(res)

reverse = lambda str: str[-1] + reverse(str[:-1]) if len(str) > 1 else str
#print(reverse(2))

str = "hello world"
#print(str[:-1])
print(reverse(str))