import re

def solution(string,markers):
    escapeChars = ".^$*+-?()[]{}\|"
    #print(markers)
    for i in range(len(markers)):
        marker = markers[i]
        if marker in escapeChars:
            print(marker, "In escpae chars")
            markers[i] = "\\" + marker
    print("Markers:", markers)
    regex = ("(" + '|'.join(markers) + ")" + ".*")
    print(regex)
    
    parts = string.split("\n")
    # for s in parts:
    #     s = re.sub(regex, '', s)
    #     print(s)
    #     #s = s.split(markers)
    #     #print(s)
    # print(s)
    parts = [str(re.sub(regex, '', s)).strip() for s in parts]
    print(parts)
    return '\n.join(parts)




solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]) #===>, "apples, pears\ngrapes\nbananas")
solution("a #b\nc\nd $e f g", ["#", "$"]) #===>, "a\nc\nd")