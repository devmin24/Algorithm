# 백준 2839 설탕 배달
n = int(input()) 
box = 0
while n >= 0 :
    if (n%5) == 0 :
        box = box + (n//5)
        print(box)
        break
    n = n-3
    box += 1
else : 
    print(-1)