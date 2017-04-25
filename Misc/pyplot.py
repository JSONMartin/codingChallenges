import matplotlib.pyplot

def createGraph():
    x_nums = [1, 2, 3]
    y_nums = [2, 4, 6]

    matplotlib.pyplot.plot(x_nums, y_nums)
    matplotlib.pyplot.show()

createGraph()