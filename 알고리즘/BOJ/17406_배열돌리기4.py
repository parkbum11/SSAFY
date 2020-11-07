import sys
sys.stdin = open('input.txt', 'r')

# 소요시간 : 1h
# 푼 날짜 : 20.10.24

import copy
from itertools import permutations
def rotation(r, c, s):
    cnt = 0
    for i in range(1, s+1):
        dumy = arr[r][c]
        dir = 0
        r -= 1
        c -= 1
        while dir != 4:
            if dumy:
                copy_arr[r][c], dumy = dumy, copy_arr[r][c]
            else:
                dumy = copy_arr[r][c]
            r += dr[dir]
            c += dc[dir]
            cnt += 1
            if cnt == i*2:
                cnt = 0
                dir += 1
        copy_arr[r][c], dumy = dumy, copy_arr[r][c]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
result = 100 * 100
R, C, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
kind = [list(map(int, input().split())) for _ in range(K)]
kkind = []
for i in list(permutations(kind, K)):
    kkind.append(list(i))
for i in kkind:
    copy_arr = copy.deepcopy(arr)
    for j in i:
        r, c, s = j[0], j[1], j[2]
        rotation(r - 1, c - 1, s)
    a = 0
    for j in range(R):
        a = sum(copy_arr[j])
        if result > a:
            result = a
print(result)