import sys
sys.stdin = open('input.txt', 'r')

def check():
    global result
    new_card = [0, set(player12[1]), set(player12[2])]
    for i in range(1, 3):
        for j in new_card[i]:
            if player12[i].count(j) == 3:
                result += i
                break
            elif (j + 1) in player12[i] and (j + 2) in player12[i]:
                result += i
                break
for t in range(1, 1+int(input())):
    result = 0
    cards = list(map(int, input().split()))
    for i in range(6, 13, 2):
        player12 = [0, cards[0:i:2], cards[1:i:2]]
        check()
        if result == 3:
            result = 1
            break
        elif result != 0:
            break
    print('#{} {}'.format(t, result))