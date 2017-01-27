def split_workload(workload):
    if not workload: return (None, None)

    options = []

    for i in range(len(workload) + 1):
        options.append( (workload[:i], workload[i:]) )

    differences = [abs(sum(d[0])-sum(d[1])) for d in options]
    difference = min(differences)

    return (differences.index(difference), difference)


### TESTING

res = split_workload([1, 6, 2, 3, 5, 4, 1]) #-> (4, 2)
print(res)