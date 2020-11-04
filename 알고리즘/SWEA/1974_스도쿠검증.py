import sys
sys.stdin = open('input.txt', 'r')

# 소요시간 :
# 푼 날짜 : 2020-10-25

for t in range(1, 1+int(input())):
    result = 1
    y = [[] for _ in range(9)]
    for i in range(3):
        a = []
        b = []
        c = []
        for _ in range(3):
            li = list(map(int, input().split()))
            if len(set(li)) != 9:
                result = 0
                break
            for k in range(9):
                y[k].append(li[k])
                if 0 <= k < 3:
                    a.append(li[k])
                elif 3 <= k < 6:
                    b.append(li[k])
                else:
                    c.append(li[k])
        if result == 0:
            break
        if len(set(a)) != 9 or len(set(b)) != 9 or len(set(c)) != 9:
            result = 0
            break
    if result != 0:
        for j in y:
            if len(set(j)) != 9:
                result = 0
                break
    print('#{} {}'.format(t, result))

