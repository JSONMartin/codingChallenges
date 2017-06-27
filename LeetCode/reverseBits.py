# https://leetcode.com/problems/reverse-bits/#/description

class Solution:
    def reverseBits(self, n):
        stringBit = str(bin(n)[2:]).zfill(len('00000000000000000000000000000000'))
        print(stringBit, stringBit[::-1])
        return int(stringBit[::-1], 2)

### TESTING ###
res = Solution().reverseBits(2)
print(res)