import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def bfs():
    q = deque()

n = int(input())
li = [[False] * (n + 1) for _ in range(n + 1)]
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    li[x][y] = li[y][x] = True
bfs()