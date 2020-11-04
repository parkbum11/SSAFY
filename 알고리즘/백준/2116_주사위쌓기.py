import sys
sys.stdin = open("input.txt", "r")

N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]
info = [0, 1, 2, 5, 3, 4]
result = 0
for first_dice in dices[0]:
    maxx = 0
    index_info = [first_dice]
    for d in range(N):
        a = dices[d].index(index_info[0])
        infoo = (info.index(a) + 3) % 6
        index_info.append(dices[d][info[infoo]])
        max_num = 0
        for dd in dices[d]:
            if dd not in index_info and max_num < dd:
                max_num = dd
        index_info.pop(0)
        maxx += max_num
    if maxx > result:
        result = maxx
print(result)
