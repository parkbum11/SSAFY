s = 'aaaabbbbc'
alphabet = []
n = 1
count_alphabet = []
for i in s:
    if i in alphabet: count_alphabet[alphabet.index(i)] += 1
    else: alphabet.append(i); count_alphabet.append(1)
result = max(count_alphabet) - min(count_alphabet)
cnt = 1
while cnt <= n and result != 0:
    for i in range(len(count_alphabet)):
        count_alphabet[i] -= cnt
        minn = 50
        for i in count_alphabet:
            if i < minn and i != 0: minn = i
        if max(count_alphabet) - minn < result:
            result = max(count_alphabet) - minn
        count_alphabet[i] + cnt
    cnt += 1
print(result)
