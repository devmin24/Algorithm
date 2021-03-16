# 백준 1010 다리놓기

from math import factorial

n = int(input())

for i in range(n) :
    k,n = map(int,input().split())
    b = factorial(n)// (factorial(k)*(factorial(n-k)))
    print(b)