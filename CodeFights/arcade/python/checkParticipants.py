def checkParticipants(participants):
    return [idx for (idx, participant) in enumerate(participants) if participant < idx]


# TESTS
test1 = [0, 1, 1, 5, 4, 8]
checkParticipants(test1)
