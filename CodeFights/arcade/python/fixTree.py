def fixTree(tree):
    return list(map(lambda x: x.strip().center(len(max(tree)), ' '), tree))
