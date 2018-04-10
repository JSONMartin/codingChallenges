def isTestSolvable(ids, k):
    digitSum = lambda qId: sum(map(int, str(qId)))

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0
