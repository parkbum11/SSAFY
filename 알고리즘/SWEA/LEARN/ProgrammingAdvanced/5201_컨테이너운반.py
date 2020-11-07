import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    boxs = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    boxs.sort(reverse=True)
    trucks.sort(reverse=True)
    result, box_index, trucks_index = 0, 0, 0
    while (box_index != N) and (trucks_index != M):
        if trucks[trucks_index] >= boxs[box_index]:
            result += boxs[box_index]
            box_index += 1
            trucks_index += 1
        else: box_index += 1
    print('#{} {}'.format(t, result))
