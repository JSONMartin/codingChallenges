class Solution(object):
    # Improved One Line solution
    def lengthOfLastWord(self, s): return len(s.strip().split("")[-1])

    def lengthOfLastWordFirstSubmission(self, s): 
        words = s.split(' ')
        words = [word for word in words if word != '']
        
        if len(words) >= 1:
            return len(words[-1])
        else: return 0