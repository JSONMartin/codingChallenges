def makeArrayConsecutive2(statuses):
    minimum, maximum = min(statuses), max(statuses)
    spread = abs(maximum - minimum)

    difference = spread - len(statuses) + 1

    return difference
