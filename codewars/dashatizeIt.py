"""
# https://www.codewars.com/kata/58223370aef9fc03fd000071/train/python
Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'
"""
def dashatize(num):
    try:
        num = abs(num)
        result = ""
        
        for i in str(num):
            if int(i) % 2 != 0:
                result += "-{}-".format(i)
            else:
                result += i
        
        result = result.replace('--', '-').strip('-')
        return result
    except:
        return 'None'



dashatize(-1)