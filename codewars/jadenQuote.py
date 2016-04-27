def toJadenCase(string):
    split_str = string.split(' ')
    return_str = ""
    for word in split_str:
        return_str += word.capitalize() + " "
    return return_str.rstrip(" ")


quote = "How can mirrors be real if our eyes aren't real"
print toJadenCase(quote)