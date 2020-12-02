import sys
sys.stdin = open('input.txt', 'r')

def hiking(r, c, broken_cnt, broken_num, broken_r, broken_c, cnt):
    global result
    if broken_cnt > 1:
        if cnt - 1 > result:
            result = cnt - 1
        return
    ccc = 0
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if rr < 0 or rr >= N or cc < 0 or cc >= N: continue
        if flag[rr][cc] == True: continue
        if broken_cnt:
            if broken_r == r and broken_c == c:
                if arr[r][c] - broken_num > arr[rr][cc]:
                    flag[rr][cc] = True
                    hiking(rr, cc, broken_cnt, broken_num, broken_r, broken_c, cnt + 1)
                    flag[rr][cc] = False
                    ccc += 1
                elif arr[r][c] - broken_num > arr[rr][cc] - K:
                    flag[rr][cc] = True
                    hiking(rr, cc, broken_cnt + 1, arr[rr][cc] - arr[r][c] + 1, rr, cc, cnt + 1)
                    flag[rr][cc] = False
                    ccc += 1
            else:
                if arr[r][c] > arr[rr][cc]:
                    flag[rr][cc] = True
                    hiking(rr, cc, broken_cnt, broken_num, broken_r, broken_c, cnt + 1)
                    flag[rr][cc] = False
                    ccc += 1
                elif arr[r][c] > arr[rr][cc] - K:
                    flag[rr][cc] = True
                    hiking(rr, cc, broken_cnt + 1, arr[rr][cc] - arr[r][c] + 1, rr, cc, cnt + 1)
                    flag[rr][cc] = False
                    ccc += 1
        else:
            if arr[r][c] > arr[rr][cc]:
                flag[rr][cc] = True
                hiking(rr, cc, broken_cnt, broken_num, broken_r, broken_c, cnt + 1)
                flag[rr][cc] = False
                ccc += 1
            elif arr[r][c] > arr[rr][cc] - K:
                flag[rr][cc] = True
                hiking(rr, cc, broken_cnt + 1, arr[rr][cc] - arr[r][c] + 1, rr, cc, cnt + 1)
                flag[rr][cc] = False
                ccc += 1
    if not ccc:
        if cnt > result:
            result = cnt
        return
dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
for t in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    mountain_top_depth = 0
    arr = []
    for _ in range(N):
        ar = list(map(int, input().split()))
        arr.append(ar)
        if max(ar) > mountain_top_depth: mountain_top_depth = max(ar)
    result = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == mountain_top_depth:
                flag = [[False] * N for _ in range(N)]
                flag[i][j] = True
                hiking(i, j, 0, 0, -1, -1, 1)
    print('#{} {}'.format(t, result))