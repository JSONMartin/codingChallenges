# http://www.codewars.com/kata/538ae2eb7a4ba8c99b000439


# RegEx method
import re
def autocorrect(input):
    regex = r"\b(u|you+)\b"
    return re.sub(regex, "your sister", input, flags=re.IGNORECASE)

# Iterative method
# import string
# def autocorrect(input):
#     def replace(word):
#         orig_word = word
#         word = "".join(c for c in word.lower() if c not in string.punctuation)
#         correction = "your sister" + "".join(c for c in orig_word if c in string.punctuation)
#         if word == 'u': return correction
#         if word[:3] == 'you' and word[3:] == 'u'*(len(word)-3) : return correction
#         else: return orig_word
#     words = input.split(" ")
#     words = map(replace, words)
#     return ' '.join(words)

'''
TESTS
'''

print(autocorrect("u"))
print(autocorrect("you"))
print(autocorrect("Youuuuu"))
print(autocorrect("youtube"))
print(autocorrect("I miss you!"))
