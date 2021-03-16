# 백준 4948번 베르트랑 공준
import math
import sys

def num(num): # 소수 구하는 함수 3 5 7 11 ...
    if num == 1:
        return False
    else :
        for i in range(2,int(math.sqrt(num))+1) :
            if num%i == 0:
                return False
        return True

all_list = list(range(2,246912)) # 문제에서 주어진 범위
save_list=[]

for i in all_list : # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
    if num(i):
        save_list.append(i)


num = int(sys.stdin.readline())

while num != 0:
    count = 0
    for i in save_list: # 저장된 소수들 중,
        if num < i <= num*2:
            count += 1
    print(count)
    num = int(sys.stdin.readline())