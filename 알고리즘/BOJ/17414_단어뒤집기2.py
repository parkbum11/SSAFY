import sys
sys.stdin = open('input.txt', 'r')

words = list(input())
words_length = len(words)
cnt = 0
while cnt < words_length:
    if words[cnt] == '<':
        for i in range(cnt + 1, words_length):
            if words[i] == '>':
                break
        cnt = i + 1
    elif words[cnt] == ' ':
        for i in range(cnt + 1, words_length):
            if words[i] != ' ' or words[i] != '<':
                break
        cnt = i
    else:
        for i in range(cnt + 1, words_length):
            if words[i] == ' ' or words[i] == '<':
                end, r_end = (i - 1), i
                break
        else: end, r_end = (words_length - 1), words_length
        while cnt < end:
            words[cnt], words[end] = words[end], words[cnt]
            cnt += 1
            end -= 1
        cnt = r_end
print(''.join(words))