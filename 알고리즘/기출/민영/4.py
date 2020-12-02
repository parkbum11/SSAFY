result = 0
length = len(cardnum)
if not length & 1:
    cardnum = '0' + cardnum
for i in range(len(cardnum)):
    num = int(cardnum[i])
    a = 0
    if i & 1:
        a += (num * 2)
    else:
        a += num
    if a >= 10:
        result += (a % 10); result += 1
    else:
        result += a
if result % 10: print('INVALID')
else: print('VALID')