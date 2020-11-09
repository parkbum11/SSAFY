import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
def cal():
    global result
    st, en, i, summ = 0, 0, 2, numerical[0]
    while i < N:
        if not st or not en:
            if len(a): st, en = a.popleft()
        if i == st:
            if numerical[i + 1] == '+': summm = numerical[i] + numerical[i + 2]
            elif numerical[i + 1] == '-': summm = numerical[i] - numerical[i + 2]
            else: summm = numerical[i] * numerical[i + 2]
            st, en, i_help = 0, 0, 2
        else: summm = numerical[i]; i_help = 1
        if numerical[i - 1] == '+': summ += summm
        elif numerical[i - 1] == '-': summ -= summm
        else: summ *= summm
        i += 2 * i_help
    if summ > result: result = summ
# main
N = int(input())
numerical = list(input()) + [0]
result = -2147483648
# int 형으로 변환
for i in range(0, len(numerical), 2):
    numerical[i] = int(numerical[i])
# 괄호가 들어 갈 수 있는 곳 저장
cal_info = []
for i in range(2, N - 1, 2):
    cal_info.append((i, i + 3))
# 여러개의 괄호가 들어 갈 수 있기 때문에 중복이 없는 순열을 만듬 use bit cal
n = len(cal_info)
for i in range(1 << n):
    a = deque()
    for j in range(n):
        if i & (1 << j):
            a.append((cal_info[j]))
    if len(a) == 0: continue
    elif len(a) == 1: cal()
    else:
        for aa in range(1, len(a)):
            if a[aa - 1][1] > a[aa][0]: break
        else: cal()
a = []; cal()
print(result)

# 1등 코드
# j=int
# def g(x,y,c):return x+y if c=='+'else x-y if c=='-'else x*y
# def f(i,c): if i>=n else max(f(i+2,g(c,j(s[i]),s[i-1])),f(i+4,g(c,g(j(s[i]),j(s[i+2]),s[i+1]),s[i-1]))if i<n-2 else -99)
# n,s=j(input()),input()
# print(f(2,j(s[0])))