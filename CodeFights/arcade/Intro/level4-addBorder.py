def addBorder(picture):
    result = []

    for row in picture:
        result.append('*%s*' % row)

    border = '*' * len(result[0])

    result = [border] + result + [border]

    return result
