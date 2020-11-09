import sys
sys.stdin = open('input.txt', 'r')

def move(now, cnt):
    global result
    visited[now] = True
    if cnt > result: return
    if now == G:
        if cnt < result: result = cnt
        return
    if 1 <= now + U <= F and visited[now + U] == False:
        move(now + U, cnt + 1)
    elif 1 <= now - D <= F and visited[now - D] == False:
        move(now - D, cnt + 1)
# main
from collections import deque
F, S, G, U, D = map(int, input().split())
result = 987654321
visited = [False] * (F+1)
q = deque()
q.append((S, 0))
while len(q):
    now, cnt = q.popleft()
    if now == G:
        if cnt < result: result = cnt
        break
    if 1 <= now + U <= F and visited[now + U] == False:
        visited[now + U] = True
        q.append((now + U, cnt + 1))
    if 1 <= now - D <= F and visited[now - D] == False:
        visited[now - D] = True
        q.append((now - D, cnt + 1))
if result == 987654321: print('use the stairs')
else: print(result)