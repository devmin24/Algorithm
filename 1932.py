# 백준 1932 정수 삼각형
n = int(input())
t = []

for i in range(n):
    t.append(list(map(int, input().split())))
k = 2
for i in range(1, n): # i = 1,2,3,4
    for j in range(k): # j = 0,1 / 0,1,2 / 0,1,2,3 / 0,1,2,3,4
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j] # 맨 앞자리
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1] # 맨 뒷자리
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j] # 나머지(가운데)는 자기 기준으로 왼쪽,오른쪽과 비교하여 큰 값을 더한다.
    k += 1
print(max(t[n - 1]))