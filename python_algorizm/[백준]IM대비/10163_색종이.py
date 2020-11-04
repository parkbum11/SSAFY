import sys
sys.stdin = open("input.txt", "r")

arr = [[False] * 101 for _ in range(101)]
N = int(input())
for n in range(1, N+1):
    st, en, w, h = map(int, input().split())
    for i in range(st, st+w):
        for j in range(en, en+h):
            arr[i][j] = n
result = {}
for i in range(101):
    for j in range(101):
        if arr[i][j]:
            if arr[i][j] in result:
                result[arr[i][j]] += 1
            else:
                result[arr[i][j]] = 1
for n in range(1, N+1):
    if n in result:
        print('{}'.format(result[n]))
    else:
        print(0)