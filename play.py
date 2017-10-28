import re

# phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
# testLa = phoneNumRegex.search('My number is 415-355-4242. 123-456-7890')
# print(f"foundNum:{testLa.groups()}")

match = phoneNumRegex.findall('Cell: 415-555-9999, Work: 215-123-4568, Test: 123-456-7890')
print(match)

# batRegex = re.compile(r'(Bat)(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile lost a wheel')
# print(mo.group())
# print(mo.group(2))

# batRegex = re.compile(r'Bat(wo)*man')
# mo = batRegex.search('lala pfft Batwowowowowowowoman')
# print(mo.group())

# greedyHaRegex = re.compile(r'(Ha){3,5}')
# match1 = greedyHaRegex.search('HaHaHaHaHa')
# print(match1.group())

# nonGreedyHaRegex = re.compile(r'(Ha){3,5}?')
# match2 = nonGreedyHaRegex.search('HaHaHaHaHa')
# print(match2.group())

# namesRegex = re.compile(r'Agent \w+')
# print(namesRegex.sub('CENSORED NAME', 'Agent Alice gave the secret docuemnts to Agent Bob.'))
# namesRegex = re.compile(r'Agent (\w)(\w*)')
# print(namesRegex.findall('Agent Alice gave the secret docuemnts to Agent Bob, then Agent Susan said LALA to Agent Carol.'))
# print(namesRegex.sub(r'\1****', 'Agent Alice gave the secret docuemnts to Agent Bob, then Agent Susan said LALA to Agent Carol.'))

# #########################
# # Verbose mode for breaking up regex with whitespace to enhance readability!
# #########################
# phoneRegex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?            # area code
#     (\s|-|\.)?                    # separator
#     \d{3}                         # first 3 digits
#     (\s|-|\.)                     # separator
#     \d{4}                         # last 4 digits
#     (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
# )''', re.VERBOSE);

# Excerpt From: Al Sweigart. “Automate the Boring Stuff with Python: Practical Programming for Total Beginners.” iBooks.
# 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
# '42'
# '1,234'
# '6,368,745'
# but not the following:
# 12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)
# numberMatchRegex = re.compile(r'\d{4,}')

# numberMatchRegex = re.compile(r'\d{4,}|,\d{0,2}\D')
numberMatchRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
tests = ['42', '1,234', '6,368,745', '12,34,567', '1234']
for test in tests:
    print(test, numberMatchRegex.search(test))

print("---------------------------------------------------------------------")

# How would you write a regex that matches the full name of someone whose last name is Nakamoto?
# You can assume that the first name that comes before it will always be one word that begins with a capital letter.
#
# The regex must match the following:
# 'Satoshi Nakamoto'
# 'Alice Nakamoto'
# 'RoboCop Nakamoto'
# but not the following:
# 'satoshi Nakamoto' (where the first name is not capitalized)
# 'Mr. Nakamoto' (where the preceding word has a nonletter character)
# 'Nakamoto' (which has no first name)
# 'Satoshi nakamoto' (where Nakamoto is not capitalized)”

satoshiRegex = re.compile(r'[A-Z][a-z]+\sNakamoto')
tests = [
'Satoshi Nakamoto',
'Alice Nakamoto',
'RoboCop Nakamoto',
'satoshi Nakamoto',
'Mr. Nakamoto',
'Nakamoto',
'Satoshi nakamoto',
]
for test in tests:
    print(test, satoshiRegex.search(test))


print("---------------------------------------------------------------------")

# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol;
# the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence
# ends with a period? This regex should be case-insensitive. It must match the following:
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# but not the following:
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.”

sentenceRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).', re.IGNORECASE)
tests = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.',
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.',
]
for test in tests:
    print(test, sentenceRegex.search(test))