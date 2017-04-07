import functools

def rank(st, we, rankedPerson):
    names = st.upper().split(',')
    score = lambda c: (ord(c) - ord('A')) + 1
    scores = [(n, (len(n) + sum([score(c) for c in n])) * we[idx]) for idx, n in enumerate(names)]
    print(scores)
    scores.sort(key=lambda x: (x[1], x[0]))
    print(scores[rankedPerson])

rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4)

print(ord('Z') - ord('A'))

score = lambda c: (ord(c) - ord('A')) + 1
#print([score(c) for c in "PAUL"])
s = [score(c) for c in "PAUL"]
print(sum(s)) + len(s)
