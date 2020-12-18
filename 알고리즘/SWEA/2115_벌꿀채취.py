import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
for t in range(1, 1 + int(input())):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_li = []
    for i in range(N):
        for j in range(N - M + 1):
            if sum(arr[i][j:j + M]) <= C:
                summ = 0
                for k in arr[i][j:j + M]:
                    summ += k*k
                sum_li.append((summ, i, j, j + M - 1))
            else:
                li = arr[i][j:j + M]
                com, summ = [], 0
                for k in range(M - 1, 0, -1):
                    com.append(list(combinations(li, k)))
                for index in range(len(com)):
                    for n in com[index]:
                        if sum(n) > C: continue
                        s = 0
                        for nn in n:
                            s += nn * nn
                        if s > summ: summ = s
                sum_li.append((summ, i, j, j + M - 1))
    result = 0
    for summ, i, js, je in sum_li:
        for summ2, i2, js2, je2 in sum_li:
            summm = summ + summ2
            if summm < result: continue
            if i != i2:
                result = summm
            else:
                if js == js2 and je == je2: continue
                if js < js2 <= je or js2 < js <= je2: continue
                result = summm
    print('#{} {}'.format(t, result))