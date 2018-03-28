def growingPlant(upSpeed, downSpeed, desiredHeight):
    height, time = 0, 0

    while True:
        time += 1

        # Add height
        height += upSpeed
        if height >= desiredHeight:
            return time

        # Remove Height
        height -= downSpeed


""" TESTS """
growingPlant(10, 9, 4)
