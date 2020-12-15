import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def shoot(r, c, dir):
    while True:
        if r < 0 or r >= N or c < 0 or c >= M: return
        rr, cc = rr + move_dir[dir][0], cc + move_dir[dir][0]
        if arr[rr][cc] == '#': return
        elif arr[rr][cc] == '.' or arr[rr][cc] == '-': continue
        else:
            arr[rr][cc] = '.'
            return

for t in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    r, c, dir = -1, -1, -1
    dir = ['^', 'v', '<', '>'] # 상하좌우 0123
    move_dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    arr = []
    for i in range(N):
        arrr = input()
        if r == -1:
            for ind, a in enumerate(arrr):
                for index, d in enumerate(dir):
                    if a == d:
                        r, c, dir = i, ind, index
                        break
                if r != -1: break
        arr.append(arrr)
    order_count, orders = int(input()), input()
    for order in orders:
        if order == 'S':
            shoot(r, c, dir)