import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : not solve it yet
# 푼 날짜 : 20.10.22

from itertools import combinations
def Game(r, c):
    global cnt
    q = [(r, c)]
    v = [(r, c)]
    while len(q):
        print(q)
        x, y = q.pop(0)
        for i in range(3):
            rr = x + dr[i]
            cc = y + dc[i]
            if rr <= 0 or rr > N or cc < 0 or cc >= M:
                continue
            elif arr[rr][cc] == 0 and (rr, cc) not in v:
                if (rr + abs(cc - c) - r + 1) < D:
                    v.append((rr, cc))
                    q.append((rr, cc))
                else:
                    return
            elif arr[rr][cc] == 1 and (rr, cc) not in visitied:
                visitied.append((rr, cc))
                cnt += 1
                return
N, M, D = map(int, input().split())
arr = [[0]]
result = 0
dr = [0, 0, 1]
dc = [-1, 1, 0]
attack = []
# 궁수 만들기
for i in range(0, M):
    attack.append(i)
# 거꾸로 input
for _ in range(N):
    a = list(map(int, input().split()))
    arr.insert(1, a)
# 궁수 부분집합
position = combinations(attack, 3)
for p in position:
    cnt, c = 0, 1
    visitied = []
    p1, p2, p3 = p
    positions = [p1, p2, p3]
    while c != N+1:
        for i in positions:
            if arr[c][i] == 1 and (c, i) not in visitied:
                visitied.append((c, i))
                cnt += 1
            elif D > 1:
                Game(c, i)
        # 다음 스테이지
        c += 1
    if cnt > result:
        result = cnt
print(result)