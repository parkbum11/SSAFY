import sys
sys.stdin = open('input.txt', 'r')

# 시간초과
def calcu(score, calorie, flag):
    global result
    if calorie > L: return
    if score > result: result = score
    for i in range(N):
        if flag & (1 << i): continue
        calcu(score + info[i][0], calorie + info[i][1], flag | (1 << i))
for t in range(1, 1 + int(input())):
    N, L = map(int, input().split())
    info = []
    result = 0
    for _ in range(N):
        info.append(list(map(int, input().split())))
    for i in range(N):
        calcu(info[i][0], info[i][1], 2**(i))
    print('#{} {}'.format(t, result))

# 개똥같은 코드
# from itertools import combinations
# for t in range(1, 1 + int(input())):
#     N, L = map(int, input().split())
#     info = []
#     result = 0
#     for _ in range(N):
#         info.append(list(map(int, input().split())))
#     for i in range(1, N + 1):
#         for j in list(combinations(info, i)):
#             score, calorie = 0, 0
#             for k in j: score += k[0]; calorie += k[1]
#             if calorie < L and score > result: result = score
#     print('#{} {}'.format(t, result))

# 1등 코드
# def f(i, N, Cal, D, full):
#     global L, satisfied
#     if i == N:
#         if Cal <= L:
#             if D > satisfied:
#                 satisfied = D
#     elif Cal == L:
#         if D > satisfied:
#             satisfied = D
#     elif Cal > L: return
#     elif D + full < satisfied: return
#     else:
#         # 재료를 선택하거나
#         f(i + 1, N, Cal + ingredient[i][1], D + ingredient[i][0], full - ingredient[i][0])
#         # 재료를 선택하지 않거나
#         f(i + 1, N, Cal, D, full - ingredient[i][0])
# T = int(input()) + 1
# for tc in range(1, T):
#     N, L = map(int, input().split())
#     ingredient = [list(map(int, input().split())) for _ in range(N)]
#     full = 0
#     for i in range(N):
#         full += ingredient[i][0]
#     satisfied = 0
#     f(0, N, 0, 0, full)
#     print('#{0} {1}'.format(tc, satisfied))
