import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 16m
# 푼 날짜 : 20.10.14

white = [[False] * 100 for _ in range(100)]
colored_papers = int(input())
cnt = 0
for _ in range(colored_papers):
    h, v = map(int, input().split())
    for hh in range(h-1, h+9):
        for vv in range(v-1, v+9):
            white[hh][vv] = True
for i in range(100):
    for j in range(100):
        if white[i][j] == True:
            cnt += 1
print(cnt)