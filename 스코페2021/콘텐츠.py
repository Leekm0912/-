# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

temp = list(map(float, input().split()))
n, m = list(map(int, input().split()))

g = ["A", "B", "C", "D", "E"]
grade_1 = {name: value for name, value in zip(g, temp)}
grade_2 = {name: value for name, value in zip(temp, g)}

content_info = list()
for _ in range(n):
    content_info.append(input())
0
genre_info = list()
for _ in range(n):
    temp = input()
    temp_list = list()
    for t in temp:
        temp_list.append(grade_1[t])
    genre_info.append(temp_list)

o_list = list()
y_list = list()

pos = [0, 0]
for i in range(n):
    for j in range(m):
        if (content_info[i][j] == "Y"):
            y_list.append((genre_info[i][j], (i, j)))
        elif (content_info[i][j] == "O"):
            o_list.append((genre_info[i][j], (i, j)))

y_list = sorted(y_list, key=lambda y_list: (-y_list[0], y_list[1][0], y_list[1][1]))
o_list = sorted(o_list, key=lambda o_list: (-o_list[0], y_list[1][0], y_list[1][1]))

for i in y_list:
    print(grade_2[i[0]], i[0], i[1][0], i[1][1])

for i in o_list:
    print(grade_2[i[0]], i[0], i[1][0], i[1][1])