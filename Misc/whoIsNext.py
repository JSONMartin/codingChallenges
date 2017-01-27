## https://www.codewars.com/kata/double-cola/train/python

# def whoIsNext(names, r):
#     counter, idx = 0, -1
#
#     if r <= len(names): return names[r - 1]
#
#     while r > len(names):
#         idx = (idx + 1 if idx < len(names) - 1 else 0)
#         #print(names[idx])
#         for i in range(1, 3):
#             if r <= len(names): return names[idx]
#             r -= 1
#     return names[idx]

# def whoIsNext(names, r):
#     r += 1
#     counter, idx = 0, 0
#
#     while r > 1:
#         cur = names[idx]
#         print(cur)
#         counter += 1
#         #for i in range(0, r//5):
#         for i in range(0, counter//2 + 1):
#             if r <= 0: break
#             print("Drinking can #:%d" % counter)
#             r -= 1
#
#         idx = (idx + 1 if idx < len(names) - 1 else 0)
#         #r -= 1
#         # print("R:%d" % r)
#         # print(names[idx])
#         # counter += 1
#         # for i in range(counter):
#         #     r -= 1
#         # idx = (idx + 1 if idx < len(names) else 0)
#
#     #print(names[idx])
#     return names[idx]

    #print(names)
    #print(names[0])
    #return names[0]['name']

# def whoIsNext(names, r):
#     names = [{'name': n, 'turnsLeft': 1} for n in names]
#     print("R:%d" % r)
#     print(names)
#
#     while r > 1:
#         n = names.pop(0)
#         starting_turns = n['turnsLeft']
#
#         while n['turnsLeft'] > 0:
#             if r <= 0: break
#             n['turnsLeft'] -= 1
#             r -= 1
#
#         n['turnsLeft'] = starting_turns + 1
#         names.append(n)
#         r -= 1
#
#     print(names)
#     #print(names[0])
#     return names[0]['name']

## Iterative solution, works up until LARGE numbers
def whoIsNext(names, r):
    names = names[:]
    if r <= len(names): return names[r - 1]

    counter = 1
    while r > 1:
        #names.append( [names.pop(0)] * counter )
        names += ([names.pop(0)] * 2)
        r -= 1
        counter += 1

    print(names)
    print(names[0])
    return names[0]

#res = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951)
res = whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 2)
print(res)