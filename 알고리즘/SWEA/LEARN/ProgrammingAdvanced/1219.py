import sys
sys.stdin = open("input.txt", "r")

def DFS(v):




for _ in range(1, 11):
    t, N = map(int, input().split())
    li = list(map(int, input().split()))
    arr = [[0]*100 for _ in range(100)]
    visited = [0] * (N+1)
    for i in range(N):
        arr[li[i*2]][li[i*2+1]] = arr[li[i*2+1]][li[i*2]] = 1


