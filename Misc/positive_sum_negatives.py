def count_positives_sum_negatives(arr):
    count = [0,0]

    for n in arr:
        if n > 0: count[0]+=1
        if n < 0: count[1]+=n

    return count