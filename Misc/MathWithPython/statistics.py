from collections import Counter
from matplotlib import pyplot

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

def find_corr_x_y(x,y):
    n = len(x)

    # Find the sum of the products
    prod = []
    for xi,yi in zip(x,y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
        # Find the sum
        x_square_sum = sum(x_square)

        y_square=[]
    for yi in y:
        y_square.append(yi**2)
        # Find the sum
        y_square_sum = sum(y_square)

    # Use formula to calculate correlation
    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator/denominator

    return correlation


def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader) # Skip Head

        winter = []
        highest_correlated = []

        for row in reader:
            try:
                winter.append(float(row[1]))
                highest_correlated += [float(row[2])]
            except:
                continue

        return (winter, highest_correlated)

winter, highest_correlated = read_csv('/Users/jsonmartin/Google Drive/code/codingChallenges/Misc/MathWithPython/correlate-Winter_Wave.csv')
corr = find_corr_x_y(winter, highest_correlated)
print("Highest correlation: {0}".format(corr))
pyplot.scatter(winter, highest_correlated)

### TESTS

# testList = [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200, 800]
# res = mean(testList)
# print(res)
# res = median(testList)
# print(res)
# res = most_common_elements(testList)
# print(res)
# print(range(testList))

