def alternatingSums(array):
    evenTotal, oddTotal = 0, 0

    for idx, val in enumerate(array):
        if idx % 2 == 0: evenTotal += val
        else: oddTotal += val

    return [evenTotal, oddTotal]

