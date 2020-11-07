import sys
sys.stdin = open('input.txt', 'r')

# 하나 틀림.. 왜 틀렸는지 이해가 안됨....
# for t in range(1, 1 + int(input())):
#     N = int(input())
#     result, end = 1, 0
#     timetable = [0] * 25
#     for _ in range(N):
#         st, en = map(int, input().split())
#         if timetable[en] < st:  timetable[en] = st
#     for endTime, startTime in enumerate(timetable):
#         if startTime == 0: continue
#         if not end: end = endTime
#         elif end <= startTime: result += 1; end = endTime
#     print('#{} {}'.format(t, result))

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    times = []
    for n in range(N):
        s,e = map(int,input().split())
        times.append([s,e])
    times.sort(key=lambda x:(x[1],x[0]))
    start,end = times[0]
    cnt = 1
    for t in range(1,len(times)):
        if times[t][0] >= end:
            start,end = times[t]
            cnt+=1
    print('#{} {}'.format(tc,cnt))