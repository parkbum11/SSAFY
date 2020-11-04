import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 1h이상 (균t 참고)
# 푼 날짜 : 20.10.18

def check(nums):
    global ans
    cnt = 1
    for i in range(1, N):
        if nums[i-1] <= nums[i]:
            cnt += 1
        else:
            if ans < cnt:
                ans = cnt
            cnt = 1
    if ans < cnt:
        ans = cnt
N = int(input())
arr = list(map(int, input().split()))
ans = 1
check(arr)
check(arr[::-1])
print(ans)