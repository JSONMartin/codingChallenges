from collections import Counter

# Average
def mean(nums): return sum(nums) / len(nums)

# Middle value (odd length) or average (even length) from sorted list
def median(nums):
    mid = len(nums) / 2
    nums = sorted(nums)
    return nums[int(mid)] if mid % 2 == 0 else mean(nums[int(mid)-1:int(mid)+1])

# Returns list of frequency elements
def most_common_elements(nums):
    c = Counter(nums)
    return c.most_common()[0][0]

# Print most common element table
def frequency_table(nums):
    table = Counter(nums)
    HEADER = "Number\tFrequency"
    print(HEADER + "\n" + "-"*len(HEADER))
    for n in table.most_common():
        print("{0}\t{1}".format(n[0], n[1]))

# Returns difference between highest and lowest value
def range(nums):
    return abs(max(nums) - min(nums))



testList = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 800]
res = mean(testList)
print(res)
res = median(testList)
print(res)
res = most_common_elements(testList)
print(res)
print(range(testList))
