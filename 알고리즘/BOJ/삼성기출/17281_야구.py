import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 15:30 s
# 푼 날짜 : 20.10.23


from itertools import permutations
result = 0
N = int(input())
info = [([0] + list(map(int, input().split()))) for _ in range(N)]
batting_order = []
hitter= [2, 3, 4, 5, 6, 7, 8, 9]
# 타순 계산 순열 조합
for i in list(permutations(hitter, 8)):
    batting_order.append(list(i))
batting_order = [[2,3,4,6,7,8,9,5]]
# 타순 마다 야구 진행
for b in batting_order:
    b.insert(3, 1)
    field = [0, 0, 0]
    hit, score = 0, 0
    # 이닝 마다 게임
    for n in range(N):
        out = 0
        while out != 3:
            print('hit : {}'.format(hit))
            print('score : {}'.format(score))
            if info[n][b[hit]] == 4:
                score += (sum(field) + 1)
                field = [0, 0, 0]
            elif info[n][b[hit]] == 3:
                score += sum(field)
                field = [0, 0, 1]
            elif info[n][b[hit]] == 2:
                score += sum(field)
                if field[0] == 1:
                    score -= 1
                    field = [0, 1, 1]
                else:
                    field = [0, 1, 0]
            elif info[n][b[hit]] == 1:
                s = field.pop()
                score += s
                field.insert(0, 1)
            else:
                out += 1
            hit = (hit + 1) % 9
    if score > result:
        print(b, score)
        result = score
print(result)