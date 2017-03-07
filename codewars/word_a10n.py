import re

def abbreviate(s):
    parts, results = re.split('(\W+)', s), []

    for part in parts:
        if re.match('[^a-zA-Z]', part):
            results.append(part)
        else:
            if len(part) <= 3: results.append(part)
            else: results.append(part[0] + str(len(part) - 2) + part[-1])

    return "".join(results)

### TESTING
res = abbreviate("elephant-rides are really fun!") #=> "e6t-r3s are r4y fun!"
print(res)