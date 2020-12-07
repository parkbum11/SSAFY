import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N, direc = input().split()
    n = int(N)
    maps = [list(map(int, input().split())) for _ in range(n)]
    if direc == 'up':
        for j in range(n):
            a, b, index = 0, [], 0
            for i in range(n):
                if a == 0 and maps[i][j] != 0:
                    a = maps[i][j]
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] == a:
                    b.append(a * 2)
                    a = 0
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] != a and maps[i][j] != 0:
                    b.append(a)
                    a = maps[i][j]
                    maps[i][j] = 0
            if a != 0: b.append(a)
            for bb in b:
                maps[index][j] = bb
                index += 1
    elif direc == 'down':
        for j in range(n):
            a, b, index = 0, [], n - 1
            for i in range(n - 1, -1, -1):
                if a == 0 and maps[i][j] != 0:
                    a = maps[i][j]
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] == a:
                    b.append(a * 2)
                    a = 0
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] != a and maps[i][j] != 0:
                    b.append(a)
                    a = maps[i][j]
                    maps[i][j] = 0
            if a != 0: b.append(a)
            for bb in b:
                maps[index][j] = bb
                index -= 1
    elif direc == 'right':
        for i in range(n):
            a, b, index = 0, [], n - 1
            for j in range(n - 1, -1, -1):
                if a == 0 and maps[i][j] != 0:
                    a = maps[i][j]
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] == a:
                    b.append(a * 2)
                    a = 0
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] != a and maps[i][j] != 0:
                    b.append(a)
                    a = maps[i][j]
                    maps[i][j] = 0
            if a != 0: b.append(a)
            for bb in b:
                maps[i][index] = bb
                index -= 1
    else:
        for i in range(n):
            a, b, index = 0, [], 0
            for j in range(n):
                if a == 0 and maps[i][j] != 0:
                    a = maps[i][j]
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] == a:
                    b.append(a * 2)
                    a = 0
                    maps[i][j] = 0
                elif a != 0 and maps[i][j] != a and maps[i][j] != 0:
                    b.append(a)
                    a = maps[i][j]
                    maps[i][j] = 0
            if a != 0: b.append(a)
            for bb in b:
                maps[i][index] = bb
                index += 1
    print('#{}'.format(t))
    for i in range(n):
        for j in range(n):
            print(maps[i][j], end=' ')
        print()