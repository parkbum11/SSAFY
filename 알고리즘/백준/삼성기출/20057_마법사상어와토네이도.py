import sys
sys.stdin = open('input.txt', 'r')

# 소요시간 : 1h 30m
# 푼 날짜 : 20.10.24

def sand(amount, dir, r, c):
    global result
    heip_cnt = 0
    # 1%
    for i in range(2):
        rr, cc = r + one_dr[dir][i], c + one_dc[dir][i]
        a = (amount * 1) // 100
        if 0 <= rr < N and 0 <= cc < N:
            arr[rr][cc] += a
            heip_cnt += a
        else:
            result += a
            heip_cnt += a
    # 2%, 7%
    for i in range(1, 3):
        for j in range(2):
            rr, cc = r + (two_sev_dr[dir][j] * i), c + (two_sev_dc[dir][j] * i)
            if i == 1:
                a = (amount * 7) // 100
                if 0 <= rr < N and 0 <= cc < N:
                    arr[rr][cc] += a
                    heip_cnt += a
                else:
                    result += a
                    heip_cnt += a
            else:
                a = (amount * 2) // 100
                if 0 <= rr < N and 0 <= cc < N:
                    arr[rr][cc] += a
                    heip_cnt += a
                else:
                    result += a
                    heip_cnt += a
    # 10%
    for i in range(2):
        rr, cc = r + ten_dr[dir][i], c + ten_dc[dir][i]
        a = (amount * 10) // 100
        if 0 <= rr < N and 0 <= cc < N:
            arr[rr][cc] += a
            heip_cnt += a
        else:
            result += a
            heip_cnt += a
    # 5%
    rr, cc = r + five_dr[dir], c + five_dc[dir]
    a = (amount * 5) // 100
    if 0 <= rr < N and 0 <= cc < N:
        arr[rr][cc] += a
        heip_cnt += a
    else:
        result += a
        heip_cnt += a
    # remain sand
    rr, cc = r + dr[dir], c + dc[dir]
    a = amount - heip_cnt
    if 0 <= rr < N and 0 <= cc < N:
        arr[rr][cc] += a
        arr[r][c] = 0
    else:
        result += a

one_dr = [[-1, 1], [-1, -1], [-1, 1], [1, 1]]
one_dc = [[1, 1], [-1, 1], [-1, -1], [-1, 1]]
two_sev_dr = [[-1, 1], [0, 0], [-1, 1], [0, 0]]
two_sev_dc = [[0, 0], [-1, 1], [0, 0], [-1, 1]]
ten_dr = [[-1, 1], [1, 1], [-1, 1], [-1, -1]]
ten_dc = [[-1, -1], [-1, 1], [1, 1], [-1, 1]]
five_dr = [0, 2, 0, -2]
five_dc = [-2, 0, 2, 0]
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
dir, cnt, count, result = 0, 1, 0, 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
r = c = N//2
while True:
    if count == 2:
        count = 0
        cnt += 1
    for i in range(cnt):
        r += dr[dir]
        c += dc[dir]
        if 0 <= r < N and 0 <= c < N:
            if arr[r][c]:
                sand(arr[r][c], dir, r, c)
    if r == 0 and c == -1:
        break
    dir = (dir+1) % 4
    count += 1
print(result)