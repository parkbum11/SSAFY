import sys
sys.stdin = open("input.txt", "r")

def men(x):
    help_x = x
    while x <= switch_num:
        switchs[x] = (switchs[x] + 1) % 2
        x += help_x
def women(x):
    a = 1
    switchs[x] = (switchs[x] + 1) % 2
    while (x-a) > 0 and (x+a) <= switch_num and switchs[x-a] == switchs[x+a]:
        switchs[x-a] = (switchs[x-a] + 1) % 2
        switchs[x+a] = (switchs[x+a] + 1) % 2
        a += 1
switch_num = int(input())
switchs = [False] + list(map(int, input().split()))
students = int(input())
for _ in range(students):
    student = list(map(int, input().split()))
    if student[0] == 1:
        men(student[1])
    else:
        women(student[1])
a = 0
for i in range(1, switch_num+1):
    a += 1
    print(switchs[i], end=' ')
    if a == 20:
        a = 0
        print()