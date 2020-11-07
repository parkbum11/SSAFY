import sys
sys.stdin = open('input.txt', 'r')

# 푼 시간 : 1h 20m
# 푼 날짜 : 2020.10.25

N, K = map(int, input().split())
durability = list(map(int, input().split()))
ro = [0] * N
result, cnt, up = 0, 0, 0
while cnt < K:
    result += 1
    up = (up - 1 + (2*N)) % (2*N)
    ro.insert(0, 0)
    ro.pop()
    ro[-1] = 0
    for i in range(N-2, 0, -1):
        a = (i + 1 + up) % (2*N)
        if ro[i] == 1 and durability[a] >= 1 and ro[i+1] == 0:
            durability[a] -= 1
            ro[i] = 0
            ro[i+1] = 1
            if durability[a] == 0:
                cnt += 1
    if durability[up] != 0:
        ro[0] = 1
        durability[up] -= 1
        if durability[up] == 0:
            cnt += 1
print(result)

