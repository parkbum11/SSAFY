import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 10m
# 푼 날짜 : 20.10.14
N = int(input())
students_num = list(map(int, input().split()))
result = []
for n in range(1, N+1):
    result.insert(students_num[n-1], n)
result.reverse()
# for r in result:
#     print(r, end=' ')
print(*result)