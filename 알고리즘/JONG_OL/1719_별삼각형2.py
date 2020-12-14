import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
if n < 1 or n > 100 or m < 1 or m > 4: print('INPUT ERROR!')
else:
    if m == 1:
        for i in range(n):
            if i <= n //2: print('*' * (i + 1))
            else: print('*' * (n - i))
    elif m == 2:
        num = n // 2 + 1
        for i in range(n):
            if i < num:
                print(' ' * (num - i - 1), end='')
                print('*' * (i + 1))
            else:
                print(' ' * (num - n + i), end='')
                print('*' * (n - i))
    elif m == 3:
        for i in range(n):
            if i <= n // 2:
                print(' ' * (i), end='')
                print('*' * (n - i * 2))
            else:
                print(' ' * (n - i - 1), end='')
                print('*' * (i - (n - i - 1) + 1))
    else:
        for i in range(n):
            if i <= n // 2:
                print(' ' * i, end='')
                print('*' * (n // 2 + 1 - i))
            else:
                print(' ' * (n // 2), end='')
                print('*' * (i - 1))