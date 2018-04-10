def twoTeams(students):
    return sum([students[x] for x in range(0, len(students), 2)]) - sum([students[x] for x in range(1, len(students), 2)])
