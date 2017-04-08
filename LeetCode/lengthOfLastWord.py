class Solution(object):
    def lengthOfLastWord(self, s): 
        words = s.split(' ')
        words = [word for word in words if word != '']
        
        if len(words) >= 1:
            return len(words[-1])
        else: return 0