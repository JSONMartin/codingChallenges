import re


# Convert double %% to a placeholder character,
# then substitute all valid %x string placeholders,
# then change the placeholder character back to %
def newStyleFormatting(s):
    for regex, replaceStr in [(r'%%', '|'), (r'%[bcdeEfFgGnosXx]', '{}'), (r'\|', '%')]:
        s = re.sub(regex, replaceStr, s)

    return s


""" TESTING """

newStyleFormatting("Mls %d lji  %d  %f %o %% sldjf xxx%%xxx%x")
