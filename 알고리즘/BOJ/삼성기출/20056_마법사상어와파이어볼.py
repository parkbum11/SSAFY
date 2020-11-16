import sys
sys.stdin = open('input.txt', 'r')

# 푼 시간 : infini
# 푼 날짜 : 2020.11.15

# 매우 안좋은 코드라고 생각함.
from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
order = 0
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r][c].append((m, s, d, order))
info = deque()
while order != K:
    seperate_arr = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            while len(arr[i][j]):
                if arr[i][j][0][3] != order: break
                else:
                    m, s, d, num = arr[i][j].pop(0)
                    rr, cc = i + dr[d] * s, j + dc[d] * s
                    if rr <= 0 or rr > N or cc <= 0 or cc > N:
                        rr, cc = (rr + N - 1) % N + 1, (cc + N - 1) % N + 1
                    arr[rr][cc].append((m, s, d, num + 1))
                    seperate_arr[rr][cc] += 1
                    if seperate_arr[rr][cc] >= 2 and (rr, cc) not in info:
                        info.append((rr, cc))
    while len(info):
        r, c = info.popleft()
        check = len(arr[r][c])
        new_m, new_s, new_d, new_num = 0, 0, 0, order + 1
        while len(arr[r][c]):
            m, s, d, num = arr[r][c].pop()
            new_m += m
            new_s += s
            new_d += (d % 2)
        new_m //= 5
        if new_m == 0: continue
        new_s //= check
        if new_d == check or new_d == 0: ddd = 0
        else: ddd = 1
        for d in range(ddd, 8, 2):
            arr[r][c].append((new_m, new_s, d, new_num))
            ddd += 2
    order += 1
result = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in arr[i][j]:
            result += k[0]
print(result)