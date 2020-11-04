import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    N, xxx = input().split()
    result = ''
    for x in xxx:
        decimal = int(x, 16)
        binary = format(decimal, 'b')
        while len(binary) < 4:
            binary = '0' + binary
        result += binary
    print('#{} {}'.format(t, result))