def remote_control(cnt, current_page):
    global length, minn, page
    if cnt != 0:
        if cnt + abs(int(current_page) - page) < minn:
            minn = cnt + abs(int(current_page) - page)
    if len(current_page) > length + 1:
        return
    for i in not_broken:
        remote_control(cnt + 1, current_page + i)
page = 151241
broken = [0, 1, 2, 3, 4, 7, 8, 9]
minn = abs(page - 100)
length = len(str(page))
not_broken = []
for i in range(10):
    if i not in broken:
        not_broken.append(str(i))
remote_control(0, '')
print(minn)