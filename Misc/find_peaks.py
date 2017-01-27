# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7/solutions/python

def pick_peaks(arr):
    pos, peaks = [], []

    for x in range(1, len(arr) - 1):
        if arr[x] > arr[x-1] and arr[x] > arr[x+1]:
            pos.append(x)
            peaks.append(arr[x])
        elif arr[x] > arr[x-1] and arr[x] == arr[x+1]:
            i = x + 1
            while i <= len(arr) - 1:
                if arr[x] == arr[i]:
                    i += 1
                elif arr[x] > arr[i]:
                    pos.append(x)
                    peaks.append(arr[x])
                    break
                else:
                    break

    return { 'pos': pos, 'peaks': peaks }



#res = pickPeaks([3,2,3,6,4,1,2,3,2,1,2,3])
res = pick_peaks([3, 2, 3, 6, 4, 1, 2, 3, 2, 1, 2, 2, 2, 1])
print(res)