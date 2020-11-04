import sys
sys.stdin = open('input.txt', 'r')

def move(r, c, summ):
    global result
    if summ >= result: return
    if r == c == N - 1: result = summ; return
    for i in range(0, 4, 2):
        rr, cc = r + drc[i], c + drc[i + 1]
        if 0 <= rr < N and 0 <= cc < N:
            move(rr, cc, summ + arr[rr][cc])
drc = [0, 1, 1, 0]
for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    summ, result = arr[0][0], 999
    move(0, 0, summ)
    print('#{} {}'.format(t, result))