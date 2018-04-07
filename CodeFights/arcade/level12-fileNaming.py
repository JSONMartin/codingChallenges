"""
You are given an array of desired filenames in the order of their creation.
Since two files cannot have equal names, the one which comes later will have an addition to its name in a form of (k),
where k is the smallest positive integer such that the obtained name is not used yet.

Return an array of names that will be given to the files.

Example

For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].
"""


def fileNaming(names):
    namesList = {}
    files = []

    for name in names:
        if name in namesList:
            newName = "%s(%d)" % (name, namesList[name])

            # If the new name already exists, then increment the counter
            while newName in namesList:
                namesList[name] += 1
                newName = "%s(%d)" % (name, namesList[name])

            files += [newName]
            namesList[name] += 1
            namesList[newName] = 1
        else:
            files += [name]
            namesList[name] = 1

    return files


""" TESTS """
res = fileNaming(["a(1)",
                  "a(6)",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a"])

# res = fileNaming(["doc",
#                   "doc",
#                   "image",
#                   "doc(1)",
#                   "doc"])

print(res)
