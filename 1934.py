# 벡준 1934 최소공배수

n = int(input())

def gcd(a,b):
    if b == 0 :
        return a
    else : 
        return gcd(b,a%b)

def lcm(a,b):
    g = gcd(a,b)
    return int(g*(a/g)*(b/g))

for i in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))
