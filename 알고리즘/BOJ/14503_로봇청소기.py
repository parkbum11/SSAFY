import sys
sys.stdin = open('input.txt', 'r')

import sys
sys.setrecursionlimit(10**8)
def cleanUp(r, c, d):
    global cnt
    if maps[r][c] == 0 and (r, c) not in visited: cnt += 1; visited.append((r, c))
    for i in range(1, 5):
        dd = (d + 3*i) % 4
        rr, cc = r + dr[dd], c + dc[dd]
        if maps[rr][cc] == 0 and (rr, cc) not in visited:
            cleanUp(rr, cc, dd)
            break
    else:
        rr, cc = r + dr[(d + 2) % 4], c + dc[(d + 2) % 4]
        if maps[rr][cc] == 1: return
        else: cleanUp(rr, cc, d)
# main
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
N, M = map(int, input().split())
r, c, d = map(int, input().split()) # 0123 위오아왼
maps = [list(map(int, input().split())) for _ in range(N)]
visited, cnt = [], 0
cleanUp(r, c, d)
print(cnt)

