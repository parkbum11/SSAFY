import sys
sys.stdin = open('input.txt', 'r')


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

