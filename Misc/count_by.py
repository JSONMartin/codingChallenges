# def count_by(x, n):
#     list = []
#
#     for i in range(1, n + 1):
#         list.append(x * i)
#
#     return list

def count_by(x, n):
    return [x * i for i in range(1, n+1)]

print(list(count_by(100, 5)))