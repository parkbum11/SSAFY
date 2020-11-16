import sys
sys.stdin = open("input.txt", "r")

#좌우 판단만
def search_rl():
    dy = [-1, 1]
    for y in range(2):
        yy = start[1] + dy[y]
        if 100 > yy >= 0 and arr[(start[0])][yy] == 1:
            moveY(dy[y])
            break

#좌우 있을시 끝까지 이동 d는 방향
def moveY(d):
    while arr[(start[0])][(start[1])] == 1:
        start[1] += d
        if start[1] < 0 or start[1] >= 100:
            break
    start[1] -= d

# 도착점부터 시작점까지 거꾸로 설계
for _ in range(10):
    t = int(input())
    arr = []
    start = [1, 0]
    # 거꾸로 저장
    for i in range(100):
        r_arr = list(map(int, input().split()))
        arr.insert(0, r_arr)
    # 도착점을 찾아서 저장
    for i in range(100):
        if arr[0][i] == 2:
            start[1] += i
    # 도착점에서 시작했기 때문에 시작점을 찾으면 종료
    while start[0] != 99:
        search_rl()
        start[0] += 1
    print('#{} {}'.format(t, start[1]))