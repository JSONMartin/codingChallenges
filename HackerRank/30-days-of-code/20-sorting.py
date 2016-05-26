#!/bin/python3

import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

def sort(arr):
    done = False
    numSwaps = 0
    while done != True:
        curSwaps = 0
        for x in range(0,len(arr)):
            for i in range(x, len(arr)):
                if arr[x] > arr[i]:
                    arr[i], arr[x] = arr[x], arr[i]
                    curSwaps+=1
        numSwaps += curSwaps
        if curSwaps == 0:
            done = True

    print("Array is sorted in %d swaps." % numSwaps)
    print("First Element: %d" % arr[0])
    print("Last Element: %d" % arr[len(arr) - 1])

sort(a)
