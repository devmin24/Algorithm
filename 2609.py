# 백준 2609 최대공약수와 최소공배수

a,b = map(int,input().split())

def gcd(a,b): # 최대공약수 , 유클리드 호제법 , GCD(a,b)=GCD(b,a%b) b가 0이 될 때까지
    if b == 0 :
        return a # a의 값을 반환해라.
    else :
        return gcd(b,a%b)

def lcm(a,b): # 최소공배수 LCM(a,b) = GCD*(a/GCD)*(b/GCD)
    g = gcd(a,b)
    return int(g*(a/g)*(b/g))

print(gcd(a,b))
print(lcm(a,b))