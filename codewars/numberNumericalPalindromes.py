
"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward. Examples of numerical palindromes are:

2332 
110011 
54322345

For a given number num, write a function which returns the number of numerical palindromes within each number. For this kata, single digit numbers will NOT be considered numerical palindromes.

Return "Not valid" if the input is not an integer or is less than 0.

palindrome(5) => 0
palindrome(1221) => 2 
palindrome(141221001) => 5  
palindrome(1294) => 0
palindrome("1221") => "Not valid"
"""
def palindrome(num):
    # Alternative: if type(num) != int
    try:
        if num != int(num) or num < 0: raise Exception
        
        numStr = str(num)
        length = len(numStr)
        count = 0

        for i in range(length + 1):
            for j in range(i + 2, length + 1):
                if numStr[i:j] == numStr[i:j][::-1]: count += 1

        return count
    except:
        return "Not valid"

palindrome(141221001)