import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs():
    q = deque()
    q.append((0, 0))
    while len(q):
        r, c= q.popleft()
        if r == c == N - 1: continue
        for i in range(4):
            rr, cc = r + dr[i], c + dc[i]
            if 0 > rr or N <= rr or 0 > cc or N <= cc: continue
            if distance[rr][cc] == -1 or distance[rr][cc] > distance[r][c] + maps[rr][cc]:
                distance[rr][cc] = distance[r][c] + maps[rr][cc]
                q.append((rr, cc))
dr = [-1, 1, 0 ,0]
dc = [0, 0, -1, 1]
for t in range(1, 1 + int(input())):
    N = int(input())
    maps, distance = [list(map(int, input())) for _ in range(N)], [[-1] * N for _ in range(N)]
    distance[0][0] = maps[0][0]
    bfs()
    print('#{} {}'.format(t, distance[N - 1][N - 1]))