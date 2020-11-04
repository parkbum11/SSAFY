import sys
sys.stdin = open("input.txt", "r")

# 소요시간 :
# 푼 날짜 : 20.10.14

content = input()
N = len(content)
result = ''
R, C = 0, 0
max_R = round(N**(0.5))
for r in range(max_R, 0, -1):
    C = N//r
    if C * r == N:
        R = r
        break
print(R, C)
for r in range(R):
    for i in range(r, N, R):
        result += content[i]
print(result)
