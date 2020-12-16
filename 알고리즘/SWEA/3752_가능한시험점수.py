import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    check = [1] + [0] * sum(arr)
    visited = [0]
    for i in arr:
        li = visited[:]
        for j in li:
            if not check[i+j]:
                check[i+j] = 1
                visited.append(i+j)
    print('#{} {}'.format(t, len(visited)))