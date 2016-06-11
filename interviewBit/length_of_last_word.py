class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        #A.split(' ')
        print(A.strip().split(' '))
        return len(A.split(' ')[-1])



"""TESTS"""

s = Solution()
#sentence = "Haha jump over fence"
sentence = "Wordl   "

result = s.lengthOfLastWord(sentence)
print(result)
