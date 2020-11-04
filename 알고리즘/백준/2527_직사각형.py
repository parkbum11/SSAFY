import sys
sys.stdin = open("input.txt", "r")

# 소요시간 : 25m
# 푼 날짜 : 20.10.18

for _ in range(4):
    rectangle = list(map(int, input().split()))
    # computation_result : 0 = 논외, 1 = 같다,  2 = 안쪽
    # x축 연산
    if rectangle[0] < rectangle[4]:
        x1 = [rectangle[0], rectangle[2]]
        x2 = [rectangle[4], rectangle[6]]
    else:
        x1 = [rectangle[4], rectangle[6]]
        x2 = [rectangle[0], rectangle[2]]
    if x1[0] <= x2[0] < x1[1]:
        result_x = 2
    elif x1[1] == x2[0]:
        result_x = 1
    else:
        result_x = 0
    # y축 연산
    if rectangle[1] < rectangle[5]:
        y1 = [rectangle[1], rectangle[3]]
        y2 = [rectangle[5], rectangle[7]]
    else:
        y1 = [rectangle[5], rectangle[7]]
        y2 = [rectangle[1], rectangle[3]]
    if y1[0] <= y2[0] < y1[1]:
        result_y = 2
    elif y1[1] == y2[0]:
        result_y = 1
    else:
        result_y = 0
    # rsult : 0 = d, 1 = c, 2 = b, 4 = a
    if result_x * result_y == 0:
        print('d')
    elif result_x * result_y == 1:
        print('c')
    elif result_x * result_y == 2:
        print('b')
    elif result_x * result_y == 4:
        print('a')


# 백준에서 제일 잘푼 code
# def square(n):
#     x1, y1, x2, y2, x3, y3, x4, y4 = n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7]
#     if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
#         return 'd'
#     elif (x2 == x3 and y2 == y3) or (x3 == x2 and y1 == y4) or (x4 == x1 and y3 == y2) or (x4 == x1 and y4 == y1):
#         return 'c'
#     elif ((x3 == x2 or x4 == x1) and y3 < y2 and y4 > y1) or ((y2 == y3 or y4 == y1) and x4 > x1 and x3 < x2):
#         return 'b'
#     else:
#         return 'a'
#
# for _ in range(4):
#     s_list = list(map(int, input().split()))
#     print(square(s_list))

