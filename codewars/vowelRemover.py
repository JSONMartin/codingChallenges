# https://www.codewars.com/kata/5547929140907378f9000039/train/python
import re

shortcut = lambda x: re.sub(r'[aeiou]', '', x)

print(shortcut("Hello"))