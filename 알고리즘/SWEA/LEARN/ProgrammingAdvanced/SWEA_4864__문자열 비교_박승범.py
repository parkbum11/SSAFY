for t in range(1,int(input())+1):
    a = input()
    b = input()
    result = 0
    if a in b:
        result += 1
    print(f'#{t} {result}')