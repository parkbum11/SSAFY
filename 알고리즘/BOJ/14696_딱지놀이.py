N = int(input())
for _ in range(N):
    li = ['4', '3', '2', '1']
    A = input().split()
    B = input().split()
    for i in li:
        if A[1:].count(i) > B[1:].count(i):
            print('A')
            break
        elif A[1:].count(i) < B[1:].count(i):
            print('B')
            break
    else:
        print('D')