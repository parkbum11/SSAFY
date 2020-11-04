import sys
sys.stdin = open('input.txt', 'r')

# 소요시간 : 21
# 푼 날짜 : 2020-10-24

# 이미 풀어봤지만 회전형태로 다시 풀어보기
# 90, 180, 270 따로 구현도 해보기

for t in range(1, int(input())+1):
    N = int(input())
    li = [list(input().split()) for i in range(N)]
    r_li = [['']*3 for i in range(N)]
    print(f'#{t}')
    #1행
    for i in range(3):
        for j in range(N):
            for k in range(N):
                if i == 0:
                    r_li[j][i] += li[-(k+1)][j]
                elif i == 1:
                    r_li[j][i] += li[-(j+1)][-(k+1)]
                else:
                    r_li[j][i] += li[k][-(j+1)]
    for i in range(len(r_li)):
        for j in range(len(r_li[i])):
            print(r_li[i][j], end=' ')
        print()
