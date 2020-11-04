import sys
sys.stdin = open('input.txt', 'r')

def search():
    global result
    q = []
    for i in range(1, N + 1):
        if friends[1][i] == 1:
            q.append((i, 1))
            visited.append(i)
    while q:
        friend, cnt = q.pop(0)
        if cnt == 3: break
        else: result += 1
        for i in range(1, N + 1):
            if friends[friend][i] == 1 and i not in visited:
                visited.append(i)
                q.append((i, cnt + 1))
for t in range(1, 1 + int(input())):
    result = 0
    N, M = map(int, input().split())
    friends = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [1]
    for i in range(M):
        a, b = map(int, input().split())
        friends[a][b] = friends[b][a] = 1
    search()
    print('#{} {}'.format(t, result))