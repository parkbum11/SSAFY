import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs():
    Q=deque()
    Q.append(info[0])
    visited[0]=True

    while Q:
        p_x,p_y = Q.popleft()
        if p_x == info[-1][0] and p_y == info[-1][1]:
            return 'happy'
        for idx,(n_x,n_y) in enumerate(info):
            if not visited[idx] and abs(p_x-n_x) + abs(p_y-n_y)<=50*20:
                Q.append((n_x,n_y))
                visited[idx]=True
    return 'sad'

for tc in range(int(input())):
    N=int(input())
    info=[]
    visited = [False]*(N+2)
    for _ in range(N+2):
        a,b=map(int,input().split())
        info.append((a,b))
    print(bfs())