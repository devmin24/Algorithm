# 백준 11047 동전 0
n, k = map(int,input().split())
coin = []
count = 0

for i in range(n):
    coin.append(int(input()))

for i in range(n-1,-1,-1): # 10,9,8,7 ... 카운트다운
    if k == 0:
        break # 반복문 탈출
    if coin[i] > k :
        continue # 반복문의 처음으로 돌아가라.
    count += k // coin[i]
    k %= coin[i] # k = k % coin[i]
print(count)