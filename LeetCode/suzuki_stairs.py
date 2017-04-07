def stairs_in_20(stairs):
    total = 0

    for days in stairs:
        for steps in days:
            total += steps

    return steps

def stairs_in_20(stairs): return sum(sum(day) for day in stairs) * 20
