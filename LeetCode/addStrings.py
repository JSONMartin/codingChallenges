class Solution(object):
    def addStrings(self, num1, num2):
        def convertStringToNumber(string):
            num = 0
            length = len(string)
            
            for idx, n in enumerate(string):
                num += (10**(length - idx - 1)) * int(n)

            return num

        num1 = convertStringToNumber(num1)
        num2 = convertStringToNumber(num2)

        return str(num1 + num2)



### TEST ###
#Solution().addStrings('123', '321')
Solution().addStrings('4567', '3210')