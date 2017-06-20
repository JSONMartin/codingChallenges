"""
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
at least 3 numbers. For example ("12, 13, 15-17")
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted
string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
Courtesy of rosettacode.org
"""

def solution(numberList):
    print(numberList)
    start, end = None, None
    ranges = []
    result = ""

    # Calculate ranges
    for i in range(len(numberList) - 1):
        if not start: start, end = numberList[i], numberList[i]

        if numberList[i + 1] == end + 1: end += 1
        else:
            if start == end: ranges.append(end)
            else: ranges.append((start, end))
            start, end = None, None

    if start == None: pass
    if start != end: ranges.append((start, end))
    if (type(ranges[-1]) == tuple and ranges[-1][1] != numberList[-1]) or type(ranges[-1]) != tuple:
        ranges.append(numberList[-1])

    # Convert result ranges to string
    for r in ranges:
        if type(r) == tuple:
            joinChar = "-" if r[0]+1 != r[1] else ","
            result += "{}{}{}".format(r[0], joinChar, r[1])
        else:
            result += str(r)
        result += ","

    return result.rstrip(',')

    ### TESTS ###
#solution([-52, -49, -46, -45, -43, -41, -38, -37, -35, -34, -31, -28, -25, -22, -20, -17, -15, -12, -9, -6]) # => '-6,-3-1,3-5,7-11,14,15,17-20')
solution([-57, -55, -54, -53, -52, -51, -49, -46, -44, -43, -42, -41, -39, -36, -35, -33, -32, -30, -27]) # => '-6,-3-1,3-5,7-11,14,15,17-20')
#solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]) # => '-6,-3-1,3-5,7-11,14,15,17-20')
#solution([-3,-2,-1,2,10,15,16,18,19,20]) # => '-3--1,2,10,15,16,18-20')
#Test.assert_equals(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
#Test.assert_equals(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')

