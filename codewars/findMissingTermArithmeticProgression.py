from collections import Counter

# Since the first and last numbers are always there,
# Use those as a baseline to calculate the difference
def find_missing(sequence):
    difference = int((sequence[-1] - sequence[0]) / len(sequence))

    for idx, num in enumerate(sequence):
        if sequence[idx + 1] - num != difference:
            return num + difference

def find_missing_original(sequence):
    differences = []

    for i in range(1, len(sequence)):
        differences += [sequence[i] - sequence[i - 1]]

    counts = sorted(list(Counter(differences).items()), key=lambda l: l[1])
    difference, outlier = counts[1][0], counts[0][0]

    return sequence[differences.index(outlier) + 1] - difference

result = find_missing([1, 3, 5, 9, 11])
print(result)