# 백준 1011 Fly me to the Alpha Centauri
import math

N = int(input())

count = 0                                    #최소 작동 횟수
result = []

for _ in range(N): 5 10
    a, b = map(int, input().split())
    distance = b - a     9                 #주어진 값들간의 거리

    num = math.floor(math.sqrt(distance)) 2  #주어진 값들 사이의 거리에 루트 씌움 (제곱근) , floor처리되어 이미 정수임    
    num_jegob = num**2 4                # 정수를 제곱근으로 갖는 제곱수(ex. 9 : 9의 제곱근은 3)

    if distance == num_jegob: # 4 흰색
        count = (num*2)-1 #3

    elif num_jegob < distance <= num_jegob + num: # 5, 6 노랑
        count = (num*2)

    elif (num_jegob + num) < distance: # 7,8 파랑
        count = (num*2) + 1

    elif distance < 4: # 1,2,3
        count = distance

    result.append(count) # [이동횟수,이동횟수,이동횟수]

for x in result:
    print(x)