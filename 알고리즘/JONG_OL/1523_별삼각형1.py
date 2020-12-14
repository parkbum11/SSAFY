import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
if n < 1 or n > 100 or m < 1 or m > 3: print('INPUT ERROR!')
else:
    if m == 1:
        num = 1
        while num <= n:
            print('*' * num)
            num += 1
    elif m == 2:
        while n != 0:
            print('*' * n)
            n -= 1
    else:
        num = 2 * n - 1
        for i in range(n):
            for j in range(num):
                if j < num//2 - i: print(' ', end='')
                elif num//2 - i <= j <= num//2 + i: print('*', end='')
                else: break
            print()
