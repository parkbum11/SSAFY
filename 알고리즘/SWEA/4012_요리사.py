import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
for t in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visitied, result = [], 987654321
    for i in range(N):
        visitied.append(i)
    nums = list(combinations(visitied, N // 2))
    for i in range(len(nums) // 2):
        num = 0
        for j in list(combinations(nums[i], 2)):
            num += arr[j[0]][j[1]]
            num += arr[j[1]][j[0]]
        for j in list(combinations(nums[-(i + 1)], 2)):
            num -= arr[j[0]][j[1]]
            num -= arr[j[1]][j[0]]
        num = abs(num)
        if num < result: result = num
    print('#{} {}'.format(t, result))

# 진밤이 코드
# from itertools import combinations as cb
# for t in range(int(input())):
#     n=int(input())
#     l=[[*map(int,input().split())]for _ in range(n)]
#     a=[sum(i)+sum(j)for i,j in zip(l,zip(*l))]
#     b=sum(a)//2
#     p=[]
#     for i in cb(a,n//2):
#         p+=[abs(b-sum(i))]
#     print(f'#{t+1}',min(p))