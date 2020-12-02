goods = [5, 3, 15]
a, result = 0, 0
for i in goods:
    if i >= 50: result += (i - 10)
    else: a += i
if a >= 50: result += (a - 10)
else: result += a
print(result)