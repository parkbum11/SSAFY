import sys
sys.stdin = open("input.txt", "r")

def delta(r, c, num):
    if len(num) == 7:
        nums.add(num)
        return
    for i in range(4):
        rr = r + dr[i]
        cc = c + dc[i]
        if 0 <= rr < 4 and 0 <= cc < 4:
            delta(rr, cc, num+str(arr[rr][cc]))

for t in range(1, 1+int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    nums = set()
    for i in range(4):
        for j in range(4):
            delta(i, j, str(arr[i][j]))
    print('#{} {}'.format(t, len(nums)))