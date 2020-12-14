import sys
sys.stdin = open('input.txt', 'r')

def BFS(v):
    flag = True
    q = [(v, 0)]
    while q:
        curr_v, curr_count = q.pop(0)
        visited[curr_v] = 1
        for i in range(N + 1):
            if visited[i] == 0 and family[curr_v][i] == 1:
                if i == b:
                    return curr_count + 1
                else:
                    q.append((i, curr_count + 1))
    return -1
N = int(input())
a, b = map(int, input().split())
M = int(input())
family = [[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)
for i in range(M):
    c, d = map(int, input().split())
    family[c][d] = family[d][c] = 1
count = 0
ans = BFS(a)
print(ans)