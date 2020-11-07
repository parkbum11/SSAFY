import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 25m
# 푼 날짜 : 20.10.14

white = [[False] * 100 for _ in range(100)]
visited = []
colored_papers = int(input())
cnt = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]
for _ in range(colored_papers):
    h, v = map(int, input().split())
    for hh in range(h-1, h+9):
        for vv in range(v-1, v+9):
            white[hh][vv] = True
for i in range(100):
    for j in range(100):
        if white[i][j] == True:
            for k in range(4):
                rr = i + dr[k]
                cc = j + dc[k]
                if rr < 0 or rr > 99 or cc < 0 or cc > 99:
                    cnt += 1
                    continue
                elif white[rr][cc] == False:
                    cnt += 1
print(cnt)