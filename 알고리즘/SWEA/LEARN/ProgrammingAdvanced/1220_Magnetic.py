# 1 아래로 2 위로
import sys
sys.stdin = open("input.txt", "r")

def NS():
    global result
    stack = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 0:
                continue
            # stack이 empty 일 때
            elif len(stack) == 0 and arr[j][i] == 1:
                stack.append(arr[j][i])
                continue
            elif len(stack) == 0 and arr[j][i] == 2:
                continue
            # 같은 자성체가 들어올 경우 무조건 push
            elif stack[-1] == arr[j][i]:
                stack.append(arr[j][i])
            # stack에 있을 때 경우
            elif sum(stack) == len(stack) and stack[-1] != arr[j][i]:
                cnt += 1
                stack.append(arr[j][i])
            elif arr[j][i] == 1 and stack[-1] != arr[j][i]:
                stack = []
                stack.append(arr[j][i])
        stack = []
        result += cnt

for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    NS()
    print('#{} {}'.format(t, result))
