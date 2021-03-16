# 백준 2164 카드2

a = int(input())
n = [i for i in range(1, a+1)]

while len(n) > 1: # 리스트에 요소가 하나만 남을 때까지
    n.pop(0)
    n.append(n[0])
    n.pop(0)

print(n[0]) 


# 시간초과

# deque를 이용하여 시간 줄이기
import collections
a = int(input())
n = collections.deque([i for i in range(1, a+1)])

while len(n) > 1:
    n.popleft()  # 왼쪽 요소를 제거해라
    n.rotate(-1) # 왼쪽으로 한바퀴 돌려라

print(n[0])