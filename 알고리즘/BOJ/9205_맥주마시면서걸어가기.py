import sys
sys.stdin = open('input.txt', 'r')

def DFS(point):
    global result
    visited[point] = 1
    for i in range(N + 2):
        if visited[i] == 0 and need_beer[point][i] == True: DFS(i)
for _ in range(int(input())):
    N = int(input())
    need_beer = [[False] * (N + 2) for _ in range(N + 2)]
    visited = [0 for i in range(N + 2)]
    distance= [list(map(int, input().split())) for _ in range(N + 2)]
    for index, xy in enumerate(distance):
        x, y = xy[0], xy[1]
        for i in range(index + 1, N + 2):
            xx, yy = distance[i][0], distance[i][1]
            if abs(x - xx) + abs(y - yy) <= 1000:
                need_beer[index][i] = need_beer[i][index] = True
    DFS(0)
    if visited[N - 1] == 1: print('happy')
    else: print('sad')
