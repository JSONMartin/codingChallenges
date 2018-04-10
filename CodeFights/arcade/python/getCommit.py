def getCommit(commit):
    return re.split(r'[0?+!]', commit)[-1]
