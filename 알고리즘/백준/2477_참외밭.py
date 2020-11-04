import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 30m
# 푼 날짜 : 20.10.18

N = int(input())
all_size = []
only_dir = []
big = 1
small = 1
for _ in range(6):
    info = list(map(int ,input().split()))
    only_dir.append(info[0])
    all_size.append(info)
for d in range(6):
    if only_dir.count(only_dir[d]) == 1:
        big *= all_size[d][1]
        small *= all_size[(d+3)%6][1]
print(N * (big - small))
