import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : not finish
# 푼 날짜 : 20.10.20

def calcu(i):
    global result
    a, b = 0, 0
    for t in range(1, N + 1):
        if t in i:
            a += NoP[t]
        else:
            b += NoP[t]
    if result > abs(a - b):
        result = abs(a - b)

def check(i):
    q = []
    visited = []
    for t in range(1, N+1):
        if t not in i:
            q.append(t)
            visited.append(t)
            break
    while len(q):
        a = q.pop(0)
        for t in range(1, N + 1):
            if (t not in i) and (t not in visited) and (arr[a][t] == 1):
                q.append(t)
                visited.append(t)
    if len(visited) == (N - len(i)):
        return 1
    else:
        return 0

def DFS(i):
    if check(i) == 1:
        calcu(i)
    else:
        i.pop()
        return
    print(i)
    for d in range(1, N+1):
        if (arr[i[-1]][d] == 1) and (d not in visited):
            i.append(d)
            visited.append(d)
            DFS(i)

N = int(input())
NoP = [0] + list(map(int, input().split()))
cnt = 0
result = sum(NoP)
solo = []
arr = [[0] * (N+1) for _ in range(N+1)]
for n in range(1, N+1):
    info = list(map(int, input().split()))
    if info[0] == 0:
        cnt += 1
        solo.append(n)
    else:
        for i in range(1, info[0]+1):
            arr[info[i]][n], arr[n][info[i]] = 1, 1
if cnt >= 2:
    result = -1
elif cnt == 1:
    calcu(solo)
else:
    for i in range(1, N+1):
        visited = [i]
        DFS([i])
print(result)