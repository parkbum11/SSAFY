# import sys
# sys.stdin = open("input.txt", "r")

def search_long(s):
    max_long = 0
    for i in range(100):
        for j in range(i+1):
            a = s[j:(100-i+j)]
            if a == a[::-1]:
                max_long = len(a)
                break
        if max_long:
            break
    return(max_long)

def turn90(arr):
    temp = [[0]*100 for _ in range(100)]
    for x in range(100):
        for y in range(100):
            temp[y][100-x-1] = arr[x][y]
    return temp

for t in range(10):
    n = int(input())
    strings = [input() for _ in range(100)]
    max_num = 0
    for i in strings:
        a = search_long(i)
        if a > max_num:
            max_num = a
    new_strings = turn90(strings)
    for i in new_strings:
        a = search_long(i)
        if a > max_num:
            max_num = a
    print(f'#{n} {max_num}')
