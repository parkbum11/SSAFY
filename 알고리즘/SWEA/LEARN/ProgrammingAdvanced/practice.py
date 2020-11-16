di = [0, 0, 1, -1]  # 오른쪽, 왼쪽, 아래, 위 #여기서 위는 필요없음
dj = [1, -1, 0, 0]
ladder = []  # 함수에서 사용될 ladder선언


def check(i, j, dir):
    if ladder[i][j] == 2:
        return True  # 종료이면 True...본문에서 조건식으로 시작지점 나오게함
    elif i == 99:
        return False
    else:
        if (dir == 0) or (dir == 1):
            ni, nj = i + di[dir], j + dj[dir]
            if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] == 1:
                return check(ni, nj, dir)
            else:  # 못갔어, 그러면 아래로(dir=2) 내려감!!!!
                return check(i + 1, j, 2)
        else:  # 애초에 아래로 내려가는 중...dir=2
            for d in range(2):  # d가 dir
                ni, nj = i + di[d], j + dj[d]
                if ni >= 0 and ni < 100 and nj >= 0 and nj < 100 and ladder[ni][nj] == 1:
                    return check(ni, nj, d)
            return check(i + 1, j, 2)  # 아래로 내려가!!!!!!!
for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for j in range(100):
        if ladder[0][j] == 1:
            start.append(j)
    for s in start:
        if check(0, s, 2):
            print('#{} {}'.format(tc, s))
            break  # 답을 찾았기 떄문에 나가줌!!!!