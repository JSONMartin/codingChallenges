def sortByHeight(arr):
    arr = arr[:]
    length = len(arr)

    # Bubble Sort, skipping the -1s
    for i in range(length):
        for j in range(i + 1, length):
            if arr[i] == -1 or arr[j] == -1:
                continue
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    return arr
