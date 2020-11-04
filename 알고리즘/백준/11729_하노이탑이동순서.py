import sys
sys.stdin = open('input.txt', 'r')

# Timer :
# Date : 202-10-28

def movetop(num, arr, k, result, info):
    if num == 0:
        num += 1
    if len(arr[3]) == N:
        return
    print(arr, num, info)
    location = info[num]
    if arr[location].index(num) != 0:
        new_num = (num + 1) % (N + 1)
        movetop(new_num, arr, k, result, info)
    else:
        new_num = (num + 1) % (N + 1)
        top = [N+2] * N
        for i in range(1, 4):
            if i != location and len(arr[i]) == 0:
                top[i - 1] = N+1
            elif i != location and arr[i][0] > num:
                top[i - 1] = arr[i][0]
        if min(top) == N+2:
            movetop(new_num, arr, k, result, info)
        else:
            new_location = top.index(min(top)) + 1
            arr[location].pop(0)
            arr[new_location].insert(0, num)
            result.append([location, new_location])
            info[num] = new_location
            k += 1
            movetop(new_num, arr, k, result, info)

N = int(input())
ar = [0] + [[] for _ in range(3)]
inf = [0] + [1] * N
result = []
K = 1
if N % 2 == 0:
    ar[2].append(1)
    result.append([1, 2])
    inf[1] = 2
else:
    ar[3].append(1)
    result.append([1, 3])
    inf[1] = 3
for i in range(2, N+1):
    ar[1].append(i)
movetop(2, ar, K, result, inf)