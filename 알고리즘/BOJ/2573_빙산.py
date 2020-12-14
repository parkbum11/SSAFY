import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def BFS(r, c):
    q = deque()
    q.append((r, c))
    flag.append((r, c))
    while q:
        r, c = q.popleft()
        cnt_zero = 0
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < N and 0 <= cc < M and (rr, cc) not in flag:
                if maps[rr][cc] <= 0: cnt_zero += 1
                else: q.append((rr, cc)); flag.append((rr, cc))
        maps[r][c] -= cnt_zero
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
years = 0
while True:
    years += 1
    cnt = 0
    flag = []
    for i in range(N):
        for j in range(M):
            if maps[i][j] > 0 and (i, j) not in flag:
                cnt += 1
                if cnt > 1: break
                BFS(i, j)
        if cnt > 1: break
    if cnt != 1:
        if cnt == 0: print(0)
        elif years == 1 and cnt > 1: print(years - 1)
        else: print(years)
        break
