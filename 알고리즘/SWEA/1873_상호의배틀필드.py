import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def shoot(r, c, dir):
    while True:
        r, c = r + move_dir[dir][0], c + move_dir[dir][1]
        if r < 0 or r >= N or c < 0 or c >= M: break
        if arr[r][c] == '#': break
        elif arr[r][c] == '.' or arr[r][c] == '-': continue
        else:
            arr[r][c] = '.'
            break
for t in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    r, c, dir = -1, -1, -1
    dir_info = ['^', 'v', '<', '>'] # 상하좌우 0123
    move_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    arr = []
    for i in range(N):
        arrr = list(input())
        if r == -1:
            for ind, a in enumerate(arrr):
                for index, d in enumerate(dir_info):
                    if a == d:
                        r, c, dir = i, ind, index
                        break
                if r != -1: break
        arr.append(arrr)
    order_count, orders = int(input()), input()
    for order in orders:
        if order == 'S':
            shoot(r, c, dir)
        else:
            if order == 'U': dir = 0
            elif order == 'D': dir = 1
            elif order == 'L': dir = 2
            else: dir = 3
            rr, cc = r + move_dir[dir][0], c + move_dir[dir][1]
            if rr < 0 or rr >= N or cc < 0 or cc >= M:
                arr[r][c] = dir_info[dir]
                continue
            if arr[rr][cc] == '.':
                arr[r][c] = '.'
                r, c = rr, cc
                arr[r][c] = dir_info[dir]
            else:
                arr[r][c] = dir_info[dir]
    print('#{}'.format(t), end=' ')
    for a in arr:
        print(''.join(a))