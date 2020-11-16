import sys
sys.stdin = open("input.txt", "r")

def horizontal(x):
    temp = []
    for j in range(N):
        for i in range(N-M+1):
            a = x[j][i:i+M]
            if a == a[::-1]:
                temp += x[j][i:i+M]
                return temp
        if temp:
            break
    return 0

def turn90(y):
    temp = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            temp[j][N-i-1] = y[i][j]
    return temp

for t in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = horizontal(arr)
    if result == 0:
        result = horizontal(turn90(arr))
    print('#{} {}'.format(t, ''.join(result)))