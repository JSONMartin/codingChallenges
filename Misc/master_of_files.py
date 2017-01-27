"""
Are you a file extension master? Let's find out by checking if Bill's files are images or audio files. Please use regex if available natively for your language.

You will create 2 string methods:

isAudio/is_audio, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .mp3, .flac, .alac, or .aac.
isImage/is_image, matching 1 or + uppercase/lowercase letter(s) (combination possible), with the extension .jpg, .jpeg, .png, .bmp, or .gif.
Note that this is not a generic image/audio files checker. It's meant to be a test for Bill's files only. Bill doesn't like punctuation. He doesn't like numbers, neither. Thus, his filenames are letter-only

Rules

It should return true or false, simply.
File extensions should consist of lowercase letters and numbers only.
File names should consist of letters only (uppercase, lowercase, or both)
Good luck!
"""

import re

def check(extensions, file_name):
    parts = file_name.split(".")
    if len(parts) > 2: return False
    else:
        return (not bool(re.search(re.compile('\W'), parts[0]))
                and
                bool(re.search(re.compile(extensions), parts[1])))

def is_audio(file_name):
    return check('mp3$|flac$|alac$|aac$', file_name)

def is_img(file_name):
    return check('jpg$|jpeg$|png$|bmp$|gif$')
    parts = file_name.split(".")
    if len(parts) > 2: return False
    else:
        return (not bool(re.search(re.compile('\W|\d'), parts[0]))
                and
                bool(re.search(re.compile('jpg$|jpeg$|png$|bmp$|gif$'), parts[1])))


#res = is_audio("Nothing Else Matters.mp3")
res = is_img("icon2.jpg")
print(res)
