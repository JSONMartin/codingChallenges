## http://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

#"This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

def disemvowel(string):
    new_str = ""
    vowels = ['A', 'E', 'I', 'O', 'U']
    for char in string:
        if not any(char.upper() == v for v in vowels):
            new_str+=char
    return new_str

res = disemvowel('This website is for losers LOL!')
print res

