# 백준 1149 RGB거리

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):  # 두번째 집부터 최솟값을 구하고, 리스트에 넣어서 값을 바꾼다
    p[i]1[0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0] # 빨간집
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1] # 초록집
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2] # 파란집
print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))  # 두번째 집의 최솟값이 담긴 리스트와 세번째(마지막)집을 비교하여 최솟값을 출력한다.
