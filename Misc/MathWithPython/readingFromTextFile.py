def sum_data(filename):
    s = 0
    with open(filename) as f:
        for line in f:
            s += float(line)
    
    print("Sum of #s:{0}".format(s))

sum_data('/Users/jmartin/Library/Mobile Documents/com~apple~CloudDocs/Documents/code/codingChallenges/Misc/MathWithPython/mydata.txt')