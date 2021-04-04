# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = input().split()
n = int(n)
m = int(m)
clothes = list()

for _ in range(m):
    temp = list(map(int, input().split()))+[0]
    clothes.append(temp)
clothes.append([0]*(n+1))

basket = 0
pos = [0, 0]

while pos[0] != n and pos[1] != m:
    basket += int(clothes[pos[0]][pos[1]])
    #print(pos)
    if clothes[pos[0] + 1][pos[1]] < clothes[pos[0]][pos[1] + 1]:
        pos[1] += 1
    elif clothes[pos[0] + 1][pos[1]] > clothes[pos[0]][pos[1] + 1]:
        pos[0] += 1

print(basket)