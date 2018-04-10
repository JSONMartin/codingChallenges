def createHistogram(ch, data):
    return [ch * num for num in data]

# or


def createHistogramAlternative(ch, data):
    return list(map(lambda n: n * ch, data))
