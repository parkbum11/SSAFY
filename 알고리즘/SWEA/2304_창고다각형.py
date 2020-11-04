import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr = []
for _ in range(N):
    li = list(map(int, input().split()))
    arr.append(li)