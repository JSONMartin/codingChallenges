class Solution(object):
    def wordPattern(self, pattern, string):
        def patternMapper(array):
            patternSeen = {}
            patternResult = ''

            for i in range(len(array)):
                letter = array[i]
                if letter in patternSeen:
                    patternResult += patternSeen[letter]
                else:
                    patternSeen[letter] = str(i)
                    patternResult += patternSeen[letter]
            
            return patternResult
        
        patternMap = patternMapper(pattern)
        stringMap = patternMapper(string.split(' '))

