"""
Implement the method isSortedAndHow, which accepts an array of integers, and returns one of the following:

'yes, ascending' - if the numbers in the array are sorted in an ascending way
'yes, descending' - if the numbers in the array are sorted in a descending way
'no'
You can assume the array will always be valid, and there will always be one correct answer.
"""

def is_sorted_and_how(arr):
    LENGTH = len(arr)
    prev, cur, idx = arr[0], arr[1], 1
    
    # Check ascending
    if prev < cur:
        while idx < len(arr):
            prev = cur
            cur = arr[idx]
            if prev > cur: return 'no'
            idx += 1
        return 'yes, ascending'

    # Check descending
    else:
        while idx < len(arr):
            prev = cur
            cur = arr[idx]
            if prev < cur: return 'no'
            idx += 1
        return 'yes, descending'