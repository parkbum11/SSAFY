# a = [1, 2, 3, 4]
# print(-(1%8))
# import sys
# sys.stdin = open("input.txt", "r")
# 소요시간 : 1h
# 푼 날짜 : 2020-10-24

a = [0 ,1, 2, 3]
a.sort(reverse=True)
a[0] = -1
print(a)