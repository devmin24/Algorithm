# 백준 11050 이항 계수 1

from math import factorial

n,k = map(int,input().split())
b = factorial(n)// (factorial(k)*(factorial(n-k)))
print(b)



<번외> factorial 함수 만들기 (5 = 5*4*3*2*1=120)

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num