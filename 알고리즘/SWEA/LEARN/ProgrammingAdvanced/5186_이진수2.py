import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 1 + int(input())):
    xxx = float(input())
    result = ''
    num, summ = 1, 0
    while summ != xxx:
        if len(result) >= 13: break
        summm = summ + (0.5)**(num)
        if summm > xxx: result += '0'
        elif summm <= xxx: result += '1'; summ += (0.5)**(num)
        num += 1
    if len(result) >= 13: print('#{} overflow'.format(t))
    else: print('#{} {}'.format(t, result))