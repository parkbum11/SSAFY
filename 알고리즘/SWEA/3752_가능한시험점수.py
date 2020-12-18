import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [1] + [0] * sum(arr)
    nums = [0]
    for i in arr:
        li = nums[:]
        for j in li:
            if not visited[i + j]:
                visited[i + j] = 1
                nums.append(i + j)
    print('#{} {}'.format(t, len(nums)))

# for t in range(1, 1+int(input())):
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = []
#     for i in range(1<<n) :
#         re = []
#         for j in range(n):
#             if i & (1<<j):
#                 re.append(arr[j])
#         result.append(sum(re))
#     print('#{} {}'.format(t, result))