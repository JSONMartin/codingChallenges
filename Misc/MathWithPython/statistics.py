from collections import Counter
import math

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
def rangeDiff(nums):
    return abs(max(nums) - min(nums))

def calculate_variance(nums):
    avg = mean(nums)
    
    variance = 0
    for n in nums:
        variance += (n - avg) ** 2
    
    return variance / len(nums)

def standard_deviation(nums):
    return calculate_variance(nums) ** .5

def find_correlation_coefficientmine(x, y):
    n = min(len(x), len(y))
    totals = [xi * yi for xi, yi in zip(x, y)]
    print(totals)
    result = (n * sum([xi * yi for xi, yi in zip(x, y)])) - (sum(x) * sum(y)) / math.sqrt( ( n * sum([xi ** 2 for xi in x]) - (sum(x) ** 2)) * ( n * sum([yi ** 2 for yi in y]) - (sum(y) ** 2)))
    print(result)

def find_correlation_coefficient(x, y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi * yi)
    
    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x ** 2
    squared_sum_y = sum_y ** 2

    x_square = []
    for xi in x:
        x_square.append(xi ** 2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi ** 2)
    y_square_sum = sum(y_square)

    numerator = n * sum_prod_x_y - sum_x * sum_y
    denominator_term1 = n * x_square_sum - squared_sum_x
    denominator_term2 = n * y_square_sum - squared_sum_y
    denominator = (denominator_term1 * denominator_term2) ** .05
    return numerator / denominator

def correlation_coefficient(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = mean(x)
    avg_y = mean(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


highSchoolGrades = [90, 92, 95, 96, 87, 87, 90, 95, 98, 96]
collegeAdmissionTestScores = [85, 87, 86, 97, 96, 88, 89, 98, 98, 87]
print(pearson_def(highSchoolGrades, collegeAdmissionTestScores))

# testList = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200]
# res = mean(testList)
# print(res)
# res = median(testList)
# print(res)
# res = most_common_elements(testList)
# print(res)
# print(range(testList))
# print("---------------------------")
# print("Calculate Variance", calculate_variance(testList))
# print("Standard Deviation", standard_deviation(testList))