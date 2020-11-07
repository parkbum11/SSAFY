import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num = 2
for i in range(N+1):
    li = [N, i]
    while True:
        if (li[-2] - li[-1]) < 0:
            if len(li) > num:
                result = li[:]
                num = len(li)
            break
        else:
            li.append(li[-2] - li[-1])
print(num)
for r in result:
    print(r, end=' ')
print()
