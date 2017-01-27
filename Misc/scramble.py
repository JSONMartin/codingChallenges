# Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.
#
# For example:
# str1 is 'rkqodlw' and str2 is 'world' the output should return true.
# str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
# str1 is 'katas' and str2 is 'steak' should return false.
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered

# import collections
#
#
# def scramble(s1, s2):
#     s1_count, s2_count = collections.Counter(s1), collections.Counter(s2)
#
#     for letter in s2_count:
#         if s2_count[letter] > s1_count[letter]: return False
#
#     return True

### ALT

from collections import Counter
def scramble(s1,s2):
    return len(Counter(s2) - Counter(s1)) == 0


#########
# TESTS
#########

res = scramble('rkqodlw','world')
print(res)
# scramble('cedewaraaossoqqyt','codewars')
# scramble('katas','steak'),
# scramble('scriptjava','javascript')
# scramble('scriptingjava','javascript')