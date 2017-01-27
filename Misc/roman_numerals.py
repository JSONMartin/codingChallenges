# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    def romanToInt(self, s):
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        total = 0
        cur_string = s

        while len(cur_string) > 0:
            if cur_string[0:2] in dict:
                total += dict[cur_string[0:2]]
                cur_string = cur_string[2:]
            elif cur_string[0:1] in dict:
                total += dict[cur_string[0:1]]
                cur_string = cur_string[1:]

        return total


s = Solution()
#res = s.romanToInt('MIV')
res = s.romanToInt("CCLXXI")
print(res)