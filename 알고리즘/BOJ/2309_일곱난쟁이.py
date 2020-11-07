import sys
sys.stdin = open("input.txt", "r")

kids = []
for i in range(9):
    n = int(input())
    kids.append(n)
result = []
maxx = sum(kids)
sample = maxx
n = 0
while n <= 7:
    for i in range(n+1, 9):
        if (sample - kids[n] - kids[i]) == 100:
            kids.pop(i)
            kids.pop(n)
            break
    n += 1
    if len(kids) < 9:
        for i in sorted(kids):
            print(i)
        break





