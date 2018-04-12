def transposeDictionary(scriptByExtension):
    return sorted([x[::-1] for x in scriptByExtension.items()])
