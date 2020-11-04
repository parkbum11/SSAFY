import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 1h
# 푼 날짜 : 2020-10-20

def cir(n, d):
    side = [(1, -2), (-1, 2)]
    for i, j in side:
        numm = n + i
        if (0 <= numm < 4) and (numm not in visited):
            visited.append(numm)
            a = [(info[numm]+j), (info[n]-j)]
            for k in range(2):
                if a[k] >= 8:
                    a[k] %= 8
            if arr[numm][a[0]] != arr[n][a[1]]:
                cir(numm, -d)
                cir_result.append((numm, d))
for t in range(1, 1+int(input())):
    result = 0
    info = [0, 0, 0, 0]
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):
        num, dir = map(int, input().split())
        visited = [num-1]
        cir_result = [(num-1, -dir)]
        cir(num-1, dir)
        for n, d in cir_result:
            info[n] += d
            if info[n] < 0:
                info[n] += 8
            else:
                info[n] %= 8
    for i in range(4):
        if arr[i][info[i]] == 1:
            result += 2**i
    print('#{} {}'.format(t, result))
