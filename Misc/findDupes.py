def findDupes():  # Improved O(n) solution
    array = ["abc", "dd", "cc", "abc", "123"]
    count = {}

    for element in array:
        count[element] = count.get(element, 0) + 1
        if count[element] > 1: print("Duplicate found:", element)


def findDupesBruteForce():
    array = ["abc", "dd", "cc", "abc", "123"]

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]: print("Duplicate found:", array[i])


findDupes()  # => "abc"
