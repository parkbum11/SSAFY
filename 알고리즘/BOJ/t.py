di=[-1,0,1,0] #븍 동 남 서
dj=[0,1,0,-1]
d_L=[3,0,1,2]
d_B=[2,3,0,1]
N,M=map(int,input().split())
i,j,dir = map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(N)]
checked = [[False]*M for _ in range(N)]
cnt=0
#2번으로 돌아가고,그때 네방향을 세주는것임
flag=0
while 1:
    if 0>i or i>=N or 0>j or j>=M:
        break
    if arr[i][j]==0:
        arr[i][j] = -1 #청소완료
        cnt+=1

    #왼쪽방향 탐색
    cur_L = d_L[dir]
    ni = i+di[cur_L]
    nj = j+dj[cur_L]
    #flag는 왼쪽이 없을때, 사방탐색을 하는 횟수를 세주는 변수, flag=4가 된다는건 => 사방 모두 방문할수없음! 백을 해줘야함
    while flag<4:
        #왼쪽 청소 가능하면
        if arr[ni][nj]==0:
            i=ni
            j=nj
            dir=cur_L
            flag=0
            break
        else:
            flag+=1
            dir=d_L[dir]
            break
    #방향이 없음, 후진해야함
    if flag==4:
        back_d = d_B[dir]
        bi=i+di[back_d]
        bj=j+dj[back_d]
        if arr[bi][bj]==1:
            break
        else:
            i=bi
            j=bj
            flag=0
print(cnt)