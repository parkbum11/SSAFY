import sys
sys.stdin = open('input.txt', 'r')

# my code
from collections import deque
def BFS(r, c, n):
    q = deque()
    q.append((r, c))
    flag[r][c] = True
    while q:
        r, c = q.popleft()
        for dr, dc in dir:
            rr, cc = r + dr, c + dc
            if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
            if flag[rr][cc] == False and maps[rr][cc] > n:
                flag[rr][cc] = True
                q.append((rr, cc))
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
maps = []
result, maxx, minn = 1, 0, 0
for _ in range(N):
    arr = list(map(int, input().split()))
    if max(arr) > maxx: maxx = max(arr)
    if minn == 0: minn = min(arr)
    else:
        if min(arr) < minn: minn = min(arr)
    maps.append(arr)
if maxx != minn:
    for n in range(minn, maxx):
        flag = [[False] * N for _ in range(N)]
        cnt = 0
        for i in range(N):
            for j in range(N):
                if maps[i][j] > n and flag[i][j] == False: cnt += 1; BFS(i, j, n)
        if cnt > result: result = cnt
print(result)

# 1st code
import sys
from collections import defaultdict as dd
input = sys.stdin.readline
def Repr(a):
    if Set[a] == a:
        return a
    k = Repr(Set[a])
    Set[a] = k
    return k
def Join(a,b):
    Set[Repr(b)] = Repr(a)
def adj(p):
    yield p - w
    yield p - 1
    yield p + 1
    yield p + w

n = int(input())
w = n + 2
Set = {}
contour = dd(list)
for i in range(1, n+1):
    new = list(map(int, input().split()))
    for h, j in zip(new, range(i*w+1, (i+1)*w - 1)):
        contour[h].append(j)
heights = sorted(contour, reverse = True)
heights.pop()
fixed = []
cnt = 1
for h in heights:
    for k in contour[h]:
        Set[k]=k
    for p in contour[h]: # Connection change is made from added points(to both new and old components)
        for q in adj(p):
            if q in Set: Join(p, q)
    fixed = [p for p in fixed if Set[p] == p]
    for p in contour[h]:
        if Set[p] == p:
            fixed.append(p)
    cnt = max(cnt, len(fixed))
print(cnt)