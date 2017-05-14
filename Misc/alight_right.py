def align_right(text,width):
    t = text.split(" ")
    result, cur_line, i = "", "", 0

    while i < len(t):
        cur_word = t[i]
        if len(cur_line) + len(cur_word) <= width:
            cur_line += cur_word + " "
            i += 1
        else:
            result += cur_line.rstrip() + "\n"
            cur_line = ""
    result += cur_line.rstrip() + "\n
    
    if len(cur_line) + len(cur_word) <= width:
        cur_line += cur_word + " "
        i += 1
    else:
        result += cur_line.rstrip() + "\n"
        cur_line = ""   
    result += cur_line.rstrip() + "\n"

    lines = result.split("\n")[:-1]
    total = [(" " * (width - len(l)) + l) for l in lines]

    return "\n".join(total)









### TESTING

#res = align_right("I take up the whole line",24)
res = align_right("Two lines, I am",10)
print(res)