import sys
sys.stdin = open("input.txt", "r")

# 참고함..
N, K = map(int, input().split())
tem = list(map(int, input().split()))
maxx = sum(tem[:K])
plus = maxx
for i in range(K, N):
    plus -= tem[i-K]
    plus += tem[i]
    if plus > maxx:
        maxx = plus
print(maxx)