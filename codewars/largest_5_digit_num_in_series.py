# Source: http://www.codewars.com/kata/51675d17e0c1bed195000001/solutions/python

def solution(digits): #Refactored solution 
    return max(int(digits[i:i+5]) for i in range(len(digits)-4))

# def original_solution(digits):
#     largest_num = int(digits[0:5])
#     for i in xrange(len(digits)-4):
#         cur_num = int(digits[i:i+5])
#         if cur_num > largest_num:
#             largest_num = cur_num
#     return largest_num