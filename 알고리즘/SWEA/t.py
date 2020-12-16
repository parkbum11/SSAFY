codes = list(input())
secrets = list(input())
words = []
while secrets:
    w = secrets.pop(0)
    if w == " ":
        words.append(w)
    elif ord(w) >= 97:
        ans = codes[ord(w)-97]
        words.append(ans)
    else:
        ans = codes[ord(w)-65]
        words.append(chr(ord(ans)-32))
# print(''.join(words))
print(*words,sep='')


# codes = input()
# secrets = input()
# words = []
# for w in secrets:
#     if w == " ":
#         print(w,end='')
#     elif ord(w) >= 97:
#         ans = codes[ord(w)-97]
#         words.append(ans)
#         print(ans,end='')
#     else:
#         ans = codes[ord(w)-65]
#         words.append(chr(ord(ans)-32))
#         print(chr(ord(ans)-32), end = '')