import sys
sys.stdin = open('input.txt', 'r')

# 푼 시간 : 0849 -20m
# 푼 날짜 : 2020.10.25

# def separate(rr, cc):
#     sum_m, sum_s, dd, cn = 0, 0, 0, len(arr[rr][cc])
#     for i in range(len(arr[rr][cc])):
#         m, s, d = arr[rr][cc].pop()
#         sum_m += m
#         sum_s += s
#         dd += (d%2)
#     sum_m //= 5
#     sum_s //= cn
#     if sum_m == 0:
#         return
#     if dd == 0 or dd == cn:
#         dd = [0, 2, 4, 6]
#     else:
#         dd = [1, 3, 5, 7]
#     for i in dd:
#         r = rr + dr[i]
#         c = cc + dc[i]
#         if 0 <= r < N and 0 <= c < N and len(arr[r][c]) == 0:
#             arr[r][c].append((sum_m, sum_s, i))
#             move_info.append((r, c))
#         elif 0 <= r < N and 0 <= c < N and len(arr[r][c]) != 0:
#             arr[r][c].append((sum_m, sum_s, i))
#             if (r, c) not in separate_info:
#                 separate_info.append((r, c))
# def move(r, c, m, s, d):
#     rr = r + dr[d]*s
#     cc = c + dc[d]*s
#     arr[rr][cc].append((m, s, d))
#     move_info.append((rr, cc))
#     elif 0 <= rr < N and 0 <= cc < N and len(arr[rr][cc]) != 0:
#         arr[rr][cc].append((m, s, d))
#         if (rr, cc) not in separate_info:
#             separate_info.append((rr, cc))

def move(r, c, m, s, d):
    rr = r + dr[d]*s
    cc = c + dc[d]*s
    move_dumy.append(())


move_dumy = []
move_info = []
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1] += 1
    move_info.append((r-1, c-1, m, s, d))
while True:
    ll = len(move_info)
    for _ in range(ll):
        r, c, m, s, d = move_info.pop(0)
        if arr[r][c] == 1:
            arr[r][c] -= 1
            move(r, c, m, s, d)