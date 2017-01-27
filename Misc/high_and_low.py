# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

# Receives a number as a string
def high_and_low(numbers):
    num_list = list(map(int, numbers.split(" ")))
    low = num_list[0]
    high = num_list[0]

    for n in num_list:
        print("Low:%d, high:%d" % (low, high))
        low = min(low, n)
        high = max(high, n)

    return str(high) + " " + str(low)

res = high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")  # return "5 1"
print(res)