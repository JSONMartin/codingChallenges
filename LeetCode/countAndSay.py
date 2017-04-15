# 1211
class Solution(object):
    def countAndSay(self, n, curNum = 1, sequence = 2):
        if n == 1: return "1"
        nStr = str(curNum)
        last, curCount = None, 0
        counts = [] # Array of tuples (num, count)

        for num in nStr:
            if last and last != num:
                counts.append((last, curCount))
                curCount = 1
            else:
                curCount += 1
            last = num
        
        if curCount > 0: counts.append((last, curCount))
        
        result = ""
        for count in counts:
            result += str(count[1]) + str(count[0])

        if sequence < n:
            return self.countAndSay(n, int(result), sequence + 1)
        else:
            return result

#Tests
res = Solution().countAndSay(3)
print(res)
