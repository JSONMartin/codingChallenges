def pressureGauges(morning, evening):
    def lala(pepe):
        pass
    minimum, maximum = list(zip(*map(sorted, zip(morning, evening))))
    return [minimum, maximum]
    # print(*zip(morning, evening))
    print(list(map(sorted, zip(morning, evening))))
    print(*map(sorted, zip(morning, evening)))
    print(list(zip(*map(sorted, zip(morning, evening)))))
    # or
    # return [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]


""" TESTS """
morning = [3, 5, 2, 6]
evening = [1, 6, 6, 6]
pressureGauges(morning, evening)
