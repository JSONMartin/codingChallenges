def pascal(p):
    rows = [[1], [1, 1]]

    for _ in range(1, p):
        row = [1]
        lastRow = rows[-1]
        for j in range(len(lastRow) - 1):
            row += [sum(lastRow[j:j+2])]
        row += [1]
        rows += [row]
    return rows[:p]

### TESTS ###
pascal(5)