import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs(r, c, melts):
    q = deque()
    stack = deque()
    q.append((r, c))
    stack.append((r, c, melts))
    while len(q):
        r, c = q.popleft()
        melts_cnt = 0
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or cc < 0 or rr >= N or cc >= M: continue
            elif maps[rr][cc] != 0: q.append((rr, cc))
            else: melts_cnt += 1
        stack.append((r, c, melts_cnt))
    while len(stack):
        r, c, melts = stack.popleft()
        maps[r][c] -= melts
        if maps[r][c] < 0: maps[r][c] = 0
dr, dc = [1, -1, 0, 0], [0, 0, 1, -1]
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
while True:
    for i in range(N):
        for j in range(M):


