
# 진밤 코드
def qsort(l,r):
    if l<r:p=partition(l,r);qsort(l,p-1);qsort(p+1,r)
def partition(l,r):
    p=l
    while l<r:
        while arr[l]<arr[p] and l<r:l+=1
        while arr[r]>=arr[p] and l<r:r-=1
        if l<r:
            if l==p:p=r
            arr[l],arr[r]=arr[r],arr[l]
    arr[p],arr[r]=arr[r],arr[p]
    return r
for t in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    qsort(0,n-1)
    print(f'#{t+1}',arr[n//2])