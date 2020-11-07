import sys
sys.stdin = open('input.txt', 'r')

# 진범 코드
for t in range(int(input())):
    n,m=map(int,input().split())
    a=sorted([*map(int,input().split())])
    b=[*map(int, input().split())]
    cnt=0
    for i in b:
        l=0;r=n-1;f=0
        while l<=r:
            mid=(l+r)//2
            if i>=a[mid]:
                if i==a[mid]:cnt+=1;break
                l=mid+1
                if f==1:break
                f=1
            elif i<a[mid]:
                r=mid-1
                if f==-1:break
                f=-1
    print(f'#{t+1}',cnt)