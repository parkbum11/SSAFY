import sys
sys.stdin = open("input.txt", "r")
for t in range(1, 1+int(input())):
    strings = input()
    cnt = ['S', 'D', 'H', 'C']
    cnt_n = [13, 13, 13, 13]
    for i in range(4):
        cnt_n[i] -= strings.count(cnt[i])
    for i in range(len(strings)//3):
        if strings.count(strings[i*3:i*3+3]) > 1:
            print('#{} ERROR'.format(t))
            break
    else:
        print('#{} {} {} {} {}'.format(t, cnt_n[0], cnt_n[1], cnt_n[2], cnt_n[3]))