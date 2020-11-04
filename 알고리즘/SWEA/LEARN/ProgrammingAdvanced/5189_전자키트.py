import sys
sys.stdin = open('input.txt', 'r')

def work(flag, line, summ):
    global result
    if flag == (1 << N) - 1:
        if not result: result = summ + arr[line][0]
        elif result > summ + arr[line][0]: result = summ + arr[line][0]
        return
    for i in range(N):
        if line == i or flag & (1 << i): continue
        work(flag | 1 << i, i, summ + arr[line][i])
for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    work(1, 0, 0)
    print('#{} {}'.format(t, result))