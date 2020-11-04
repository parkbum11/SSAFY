import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
dic = {}
result = 0
for _ in range(N):
    student = ''.join(input().split())
    if student in dic:
        dic[student] += 1
    else:
        dic[student] = 1
for value in dic.values():
    if value % K:
        result += value//K + 1
    else:
        result += value//K
print(result)
