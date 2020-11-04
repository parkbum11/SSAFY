import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 30m 이상 (참고함)
# 푼 날짜 : 20.10.14

h, v = map(int, input().split())
num = int(input())
distance = []
result = 0
for _ in range(num+1):
    shop = list(map(int, input().split()))
    dis = 0
    if shop[0] == 1:
        dis = shop[1]
    elif shop[0] == 4:
        dis = h + shop[1]
    elif shop[0] == 2:
        dis = h*2 + v - shop[1]
    else:
        dis = (h+v)*2 - shop[1]
    distance.append(dis)
myposition = distance[-1]
for i in range(num):
    if abs(distance[i]-myposition) < (h+v):
        result += abs(distance[i]-myposition)
    else:
        result += (h+v)*2 - abs(distance[i]-myposition)
print(result)