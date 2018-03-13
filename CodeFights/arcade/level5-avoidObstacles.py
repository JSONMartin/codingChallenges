def avoidObstacles(inputArray):
    points = set(inputArray)
    limit = max(points) + 1

    for jumpLength in range(1, limit):
        obsticleHit = False
        for idx in range(0, limit, jumpLength):
            if idx in points:
                obsticleHit = True
                break

        if obsticleHit is False:
            return jumpLength

    return limit


# res = avoidObstacles([1, 4, 10, 6, 2])
res = avoidObstacles([5, 3, 6, 7, 9])
print(res)
