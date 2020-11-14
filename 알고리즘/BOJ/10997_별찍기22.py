N = int(input())
c = 4*(N-1)+1
rule = [0, c+1]
rule2 = [c//2, c//2]
for i in range(N*2):
    index = 0
    if i & 1:
        while index != c:
            if rule[0] <= index <= rule[1]: print(' ', end='')
            else:
                if index & 1: print(' ', end='')
                else: print('*', end='')
            index += 1
    else:
        while index != c:
            if rule[0] <= index <= rule[1]: print('*', end='')
            else:
                if index & 1: print(' ', end='')
                else: print('*', end='')
            index += 1
    rule[0] += 1
    rule[1] -= 1
    print()
for i in range(N*2-1):
    index = 0
    if i & 1:
        while index != c:
            if rule2[0] <= index <= rule2[1]: print(' ', end='')
            else:
                if index & 1: print(' ', end='')
                else: print('*', end='')
            index += 1
    else:
        while index != c:
            if rule2[0] <= index <= rule2[1]: print('*', end='')
            else:
                if index & 1: print(' ', end='')
                else: print('*', end='')
            index += 1
    rule2[0] -= 1
    rule2[1] += 1
    print()