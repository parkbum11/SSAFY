import sys
sys.stdin = open('input.txt', 'r')

# DFS 시간초과
# def DFS(location, time):
#     global result
#     if location == K:
#         if time < result: result = time
#         return
#     if time > result: return
#     if location > K:
#         DFS(location - 1, time + 1)
#     else:
#         DFS(location * 2, time + 1)
#         DFS(location + 1, time + 1)
#         DFS(location - 1, time + 1)
# N, K = map(int, input().split())
# result = K - N
# if result <= 0: print(abs(result))
# else: DFS(N, 0); print(result)

# BFS
from collections import deque
def BFS(n):
    global result
    q = deque()
    q.append((n, 0))
    flag[n] = True
    while q:
        location, time = q.popleft()
        if location == K:
            if time < result: result = time
            return
        for i in (location + 1, location * 2, location - 1):
            if 0 <= i < 100001 and flag[i] == False:
                flag[i] = True
                q.append((i, time + 1))

N, K = map(int, input().split())
result = K - N
flag = [False] * 100001
if result <= 0: print(abs(result))
else: BFS(N); print(result)
