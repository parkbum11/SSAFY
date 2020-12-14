import sys
sys.stdin = open('input.txt', 'r')

def dfs(y):
    global answer
    if y == n:
        answer += 1
        return
    for x in range(n):
        if x in col or (x + y) in diag1 or (x - y) in diag2: continue
        col.add(x)
        diag1.add(x + y)
        diag2.add(x - y)
        dfs(y+1)
        col.remove(x)
        diag1.remove(x + y)
        diag2.remove(x - y)

for t in range(1, 1 + int(input())):
    n = int(input())
    answer = 0
    col, diag1, diag2 = set(), set(), set()
    dfs(0)
    print('#{} {}'.format(t, answer))