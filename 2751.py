# 백준 2751 수 정렬하기 2

import sys
n = int(input())
list = []

for i in range(n):
    list.append(int(sys.stdin.readline()))

list = sorted(list)

for i in range(n):
    print(list[i])