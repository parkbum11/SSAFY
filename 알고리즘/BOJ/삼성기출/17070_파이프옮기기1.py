import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 50m (시간초과 해결x)
# 푼 날짜 : 20.10.20

def DFS(r, c, dir):
    global cnt
    if r == N-1 and c == N-1:
        cnt += 1
        return
    v = []
    for i in range(3):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < N and 0 <= cc < N and arr[rr][cc] == 0:
            v.append(arr[rr][cc])
            if (i == dir or dir == 2) and i < 2:
                DFS(rr, cc, i)
            elif (i == 2) and len(v) == 3:
                DFS(rr, cc, i)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 1]
dc = [1, 0, 1]
cnt = 0
DFS(0, 1, 0)
print(cnt)