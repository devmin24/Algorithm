# 백준 10773 제로

n = int(input())
list = []
for i in range(n):
    m = int(input())
    if m == 0:
        list.pop()
    else:
        list.append(m)

print(sum(list))