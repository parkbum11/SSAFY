import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def check_num():
    for r in range(N):
        for c in range(N):
            if arr[r][c] == '*': continue
            cnt = 0
            for i in range(8):
                rr, cc = r + dr[i], c + dc[i]
                if rr < 0 or cc < 0 or rr >= N or cc >= N: continue
                if arr[rr][cc] == '*': cnt += 1
            arr[r][c] = cnt

def check_zero(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        for i in range(8):
            rr, cc = r + dr[i], c + dc[i]
            if rr < 0 or cc < 0 or rr >= N or cc >= N: continue
            if arr[rr][cc] == 0 and visited[rr][cc] == False:
                q.append((rr, cc))
            visited[rr][cc] = True

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    check_num()
    result = 0
    for r in range(N):
        for c in range(N):
            if visited[r][c] == False and arr[r][c] == 0:
                result += 1
                check_zero(r, c)
    for r in range(N):
        for c in range(N):
            if visited[r][c] == False and arr[r][c] != '*':
                result += 1
                visited[r][c] = True
    print('#{} {}'.format(t, result))


# 1등 코드
# def chkzero(i, j):
#     global N, board, dy, dx
#     for d in range(8):
#         ny, nx = i + dy[d], j + dx[d]
#         if 0 <= ny < N and 0 <= nx < N:
#             if board[ny][nx] == '*': return False
#     else:
#         return True
# def DFS(i, j):
#     global N, visit, dy, dx
#     stack = [(i, j)]
#     while stack:
#         s = stack.pop()
#         si, sj = s[0], s[1]
#         for d in range(8):
#             ny, nx = si + dy[d], sj + dx[d]
#             if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
#                 visit[ny][nx] = 1
#                 if chkzero(ny, nx): stack.append((ny, nx))
# dy, dx = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
# for tc in range(int(input())):
#     N = int(input())
#     board, visit, cnt = [], list([0] * N for _ in range(N)), 0
#     for _ in range(N):
#         board.append(input())
#
#     for i in range(N):
#         for j in range(N):
#             if board[i][j] == '.' and visit[i][j] == 0 and chkzero(i, j):
#                 visit[i][j] = 1
#                 cnt += 1
#                 DFS(i, j)
#
#     for i in range(N):
#         for j in range(N):
#             if visit[i][j] == 0 and board[i][j] == '.': cnt += 1
#     print(f'#{tc + 1} {cnt}')