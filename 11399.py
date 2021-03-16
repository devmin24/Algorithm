# 백준 11399 ATM

n = int(input())
time = list(map(int,input().split()))
num = 0
time.sort()

for i in range(n): # 0 1 2 3 4
    num += sum(time[:i+1]) 
print(num)
