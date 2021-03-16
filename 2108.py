import sys
from collections import Counter

n = int(sys.stdin.readline())
num = []
for i in range(n):
    m = int(sys.stdin.readline())
    num.append(m) # [1,3,8,-2,2]

def avg(num): # 평균
    num = round(sum(num) / len(num)) # round 반올림
    return num

def mid(num): # 중앙값
    num.sort()
    i = len(num) // 2
    return num[i]

def mode(num): # 최빈값
    mode_dict = Counter(num) # 빈도수 세주는 라이브러리
    modes = mode_dict.most_common() # 빈도수 높은 순으로 정렬해줌

    if len(num) > 1:
        if modes[0][1] == modes[1][1]: #값이 여러 개이면 두번째 값 출력
            mod = modes[1][0]
        else :
            mod = modes[0][0]
    else :
        mod = modes[0][0]
    return mod

def many(num): # 범위
    num = max(num)-min(num)
    return num

print(avg(num))
print(mid(num))
print(mode(num))
print(many(num))