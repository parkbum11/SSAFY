import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    num = input()
    nums = num * 2
    result = set()
    turn_num_start, turn_num_end = 0, N // 4
    while turn_num_start != N // 4:
        for i in range(0, N, N // 4):
            result.add(nums[i + turn_num_start : i + turn_num_start + turn_num_end])
        turn_num_start += 1
    arr_result = list(result)
    arr_result.sort()
    print('#{} {}'.format(t, int(arr_result[-K], 16)))