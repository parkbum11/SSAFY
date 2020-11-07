import sys
sys.stdin = open('input.txt','r')
from pprint import pprint
# import copy

def rotate(arr):
    num = 0
    #돌린 arr을 담을 배열
    temp = [[0 for j in range(M)] for i in range(N)]

    while min(N,M)//2 > num:
        for i in range(num,N-num):
            for j in range(num,M-num):
                # 제일 처음 열이고 행이 처음부터 마지막-1행은 아래(행+1)로 이동
                if j == num and i != N-num-1:
                    temp[i+1][j] = arr[i][j]
                # 행이 마지막이고 열이 처음부터 마지막-1열은 오른쪽(열+1)로 이동
                elif i == N-num-1 and j !=M-num-1:
                    temp[i][j+1] = arr[i][j]
                # 열이 마지막이고 행이 처음+1부터 마지막행은 위쪽(행-1)로 이동
                elif j == M-num-1 and i != num:
                    temp[i-1][j] = arr[i][j]
                # 행이 처음이고 열이 처음을 제외하고 왼쪽(열-1)으로 이동
                elif i == num and j != num:
                    temp[i][j-1] = arr[i][j]
        #한범위의 테두리를 전부 돌면 num을 +1해서 범위를 좁혀줌
        num += 1
    return temp

#배열의 크기 N,M, 회전수 R
N,M,R = map(int,input().split())

#배열
arr = [list(map(int,input().split())) for _ in range(N)]
# temp = copy.deepcopy(arr)
for r in range(R):
    ans = rotate(arr)
    arr = ans
# print(ans)
for i in range(N):
    for j in range(M):
        print(ans[i][j],end=' ')
    print()