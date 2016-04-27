# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"


def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return names[0] + " likes this"
    elif len(names) == 2:
        return "%s and %s like this" % (names[0], names[1])
    elif len(names) == 3:
        return "%s, %s and %s like this" % (names[0], names[1], names[2])
    elif len(names) >= 4:
        return "%s, %s and %d others like this" % (names[0], names[1], (len(names)-2))


print likes([])
print likes(["Peter"])
print likes(["Jacob", "Alex"])
print likes(['Max', 'John', 'Mark'])
print likes(["Alex", "Jacob", "Mark", "Max"])
