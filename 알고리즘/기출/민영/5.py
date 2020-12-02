votes = [5, 7, 7]
if len(votes) == 1: print(0)
else:
    myvote = votes.pop(0)
    cnt = 0
    while myvote <= max(votes):
        votes[votes.index(max(votes))] -= 1
        myvote += 1
        cnt += 1
    print(cnt)