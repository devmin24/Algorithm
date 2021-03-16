# 백준 11651 좌표 구하기 -------------------------------------------------

# num = int(input())
# a = []

# for i in range(num):
#     [x,y] = map(int, input().split()) # 입력값을 공백을 제외하여 정수로 리스트 [x,y]에 넣어준다
#     rev = [y,x] # x,y로 받은 값을 뒤집어줌 (y 기준으로 정렬하기 위해)
#     a.append(rev) # 뒤집어준 값을 a리스트에 넣어준다
# b = sorted(a) # a에 들어간 요소들을 정렬하여 b에 넣어준다
# for i in range(num) : # x,y로 출력하기 위해 다시 순서를 뒤집어서 출력해준다.
#     print(b[i][1],b[i][0])



# 백준 2805 나무 자르기 --------------------------------------------------------
# n, m = map(int,input().split()) # n = 나무의 수 m = 필요한 나무의 길이
# tree = list(map(int,input().split())) # 그루 당 나무의 길이 리스트

# def h(m,tree) :
#     start = 1
#     end = max(tree) # 리스트 안의 나무에서 제일 키 큰 나무의 길이
    
#     while start <= end : # start가 end보다 작아지면 범위가 []없기 때문에 끝난다.
#         leng = 0 # 자른 나무 길이의 합을 담아둘 변수
#         mid = (start + end) // 2 # start ~ end 의 중간값

#         for i in tree :  # 일단 잘라보기
#             if i >= mid :  # 중간값보다 한 그루의 나무가 길이가 크다면
#                 leng += i - mid # 잘라서 leng에 넣자

#         if leng >= m : # leng(자른나무)가 m(필요한 나무의 길이)보다 크다면,
#             start = mid + 1 # 시작점을 조정하여 범위를 줄이자 (더 높이 잘라야 덜 자를수 있기 때문)
#         else : 
#             end = mid - 1 # m보다 적게 잘랐다면 end 값을 줄여서 높이의 범위를 낮추자
#     return end # 다 돌면 end를 변환해라.

# print(h(m,tree)) # 함수를 실행하면 end만 남아 높이가 출력된다.

#--------------------------------------------------------------------------------------------
# 백준 4949 균형잡힌 세상

# while True :
#     a = input()
#     stack = []

#     if a == "." :
#         break

#     for i in a :
#         if i == '[' or i == '(' :
#             stack.append(i)
#         elif i == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :
#                 stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
#             else : 
#                 stack.append(']')
#                 break
#         elif i == ')' :
#             if len(stack) != 0 and stack[-1] == '(' :
#                 stack.pop()
#             else :
#                 stack.append(')')
#                 break
#     if len(stack) == 0 :
#         print('yes')
#     else :
#         print('no')

#--------------------------------------------------------------------------------------------
# 백준 1874 스택 수열
# n = int(input())
# count = 0
# stack = []
# result = []
# no = True

# for i in range(0,n) :
#     x = int(input())

#     while count < x : 
#         count += 1
#         stack.append(count)
#         result.append("+")

#     if stack[-1] == x :
#         stack.pop()
#         result.append("-")
#     else : 
#         no = False
#         break

# if no == False : 
#     print("No")
# else : 
#     print("\n".join(result)) #리스트의 요소들을 줄바꿈으로 표현하는 법

#--------------------------------------------------------------------------------------------
# # 백준 1021 회전하는 큐
# n, m = map(int,input().split())  # [10,3]
# targets = list(map(int,input().split())) # [2,9,5]
# queue = [ i for i in range(1, n+1)] # [1,2,3,4,5,6,7,8,9,10]
# result = 0

# for i in range(m):
#     queue_len = len(queue) # 10
#     index = queue.index(targets[i]) 2 = 1 / 5 = 4 / 9 = 8
#     # print(index) # targets의 위치값 구하기

#     if index < queue_len - index : # 구하고자 하는 위치가 앞쪽에 있는 경우 앞으로 이동이 유리하다
#         while True : 
#             if queue[0] == targets[i] :
#                 del queue[0]
#                 break
#             else :
#                 queue.append(queue[0]) # 첫번째 요소를 맨 뒤에 추가하고, 첫번째 요소는 지워 이동한다.
#                 del queue[0]
#                 result += 1 # 이동횟수 + 1
#     else : 
#         while True : # 구하고자 하는 위치가 뒤쪽에 있는 경우 뒤로 이동이 유리하다
#             if queue[0] == targets[i] :
#                 del queue[0]
#                 break
#             else :
#                 queue.insert(0,queue[-1]) # 마지막 요소를 첫번째로 넣어주고 마지막 요소는 지운다.
#                 del queue[-1]
#                 result += 1 # 이동횟수 + 1
# print(result)


# ---------------------------------------------------------------
#  백준 2606 바이러스
# from sys import stdin
# read = stdin.readline # 이걸 사용하면 인풋을 대입해줄 필요없이 직접 read를 쓰면 됨
# dic={} # {1:{a,b}}
# for i in range(int(read())): # 7
#     dic[i+1] = set() # 인덱스는 0부터 시작이니까 +1 해줌
# for j in range(int(read())): # 6
#     a, b = map(int,read().split()) # [1,2][2,3][1,5][5,2][5,6][4,7]
#     dic[a].add(b) #양방향 성질
#     dic[b].add(a)

# def bfs(start):
#     queue = [start]
#     while queue:
#         for i in dic[queue.pop(0)]: # 큐(선입선출법) 첫번째꺼 지워주고 마지막에 넣어준다
#             if i not in visited: # visited에 값이 없으면
#                 visited.append(i)
#                 queue.append(i)
# visited = [] #[2,5,1,3,6]
# bfs(1) # = start = 1
# print(len(visited)-1) # 1은 숫주 그 자체이므로 감염된 컴퓨터 수를 구하기 위해 -1

# --------------------------------------------------------------------
# 백준 토마토

# from collections import deque

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs():
#     result = 0
#     while q:
#         result += 1
#         # _ 사용이유는 값이 필요하지않아서 무시한 경우이다.
#         for _ in range(len(q)):
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if 0 <= nx < n and 0 <= ny < m:
#                     if a[nx][ny] == 0:
#                         a[nx][ny] = 1
#                         q.append([nx, ny])
#     return result

# m, n = map(int, input().split())
# a, q = [], deque()
# for i in range(n):
#     row = list(map(int, input().split()))
#     for j in range(m):
#         if row[j] == 1:
#             q.append([i, j])
#     a.append(row)
# result = bfs() - 1
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:
#             print(-1)
#             exit()
# print(result)
# -----------------------------------------------------------------------
# 백준 1003 피보나치 수열

# t = int(input())
# zero = [1,0,1]
# one = [0,1,1]

# def fibo(n) : #[0,1,3]
#     if len(zero) <= n :
#         for i in range(len(zero), n+1) :
#             zero.append(zero[i-1]+zero[i-2])
#             one.append(one[i-1]+one[i-2])
#     print(zero[n],one[n])

# for i in range(t) : #[3]
#     a = int(input()) #[0,1,3]
#     fibo(a)

# -------------------------------------------------------------------------
# 백준 10815 숫자카드

# n = int(input())
# num_card = list(map(int,input().split()))
# m = int(input())
# nums = list(map(int,input().split()))

# num_card.sort()

# for i in range(m) :
#     low, high = 0, n-1
#     while low <= high :
#         mid = (low+high)//2
#         if num_card[mid] == nums[i]:
#             print(1,end=" ")
#             break
#         elif num_card[mid] < nums[i]:
#             low = mid+1
#         else:
#             high = mid-1
#         if low > high:
#             print(0,end=" ")
#             break

# ------------------------------------------------------------------------
# 백준 2164 카드2

# a = int(input())
# n = [i for i in range(1, a+1)]

# while len(n) > 1: # 리스트에 요소가 하나만 남을 때까지
#     n.pop(0)
#     n.append(n[0])
#     n.pop(0)

# print(n[0]) 


# # 시간초과

# # deque를 이용하여 시간 줄이기
# import collections
# a = int(input())
# n = collections.deque([i for i in range(1, a+1)])

# while len(n) > 1:
#     n.popleft()  # 왼쪽 요소를 제거해라
#     n.rotate(-1) # 왼쪽으로 한바퀴 돌려라

# print(n[0])

# -----------------------------------------------------------------------
# 백준 2751 수 정렬하기 2

# import sys
# n = int(input())
# list = []

# for i in range(n):
#     list.append(int(sys.stdin.readline()))

# list = sorted(list)

# for i in range(n):
#     print(list[i])

# -----------------------------------------------------------------------
# 백준 1316 그룹 단어 체커

# n = int(input()) 

# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1): #인덱스 범위 생성 0부터 len(word)-1
#         if word[index] != word[index+1]: #연속된 문자가 다를 때
#             new_word = word[index+1:] # 현재 문자의 다음부터 문자열을 새로운 변수에 저장한다
#             if new_word.count(word[index]) > 0: # 저장된 변수에 현재 문자가 하나라도 있으면
#                 error += 1 # 그룹문자가 아니기때문에 error +=1 을 해준다
#     if error == 0: # error가 없으면 그룹문자이다. (연속된 문자는 에러가 없다.)
#         group_word += 1
# print(group_word)

# -----------------------------------------------------------------------
# 백준 2839 설탕 배달
# n = int(input()) 
# box = 0
# while n >= 0 :
#     if (n%5) == 0 :
#         box = box + (n//5)
#         print(box)
#         break
#     n = n-3
#     box += 1
# else : 
#     print(-1)

# -----------------------------------------------------------------------
# 백준 1011 Fly me to the Alpha Centauri
# import math

# N = int(input())

# count = 0                                    #최소 작동 횟수
# result = []

# for _ in range(N): 5 10
#     a, b = map(int, input().split())
#     distance = b - a     9                 #주어진 값들간의 거리

#     num = math.floor(math.sqrt(distance)) 2  #주어진 값들 사이의 거리에 루트 씌움 (제곱근) , floor처리되어 이미 정수임    
#     num_jegob = num**2 4                # 정수를 제곱근으로 갖는 제곱수(ex. 9 : 9의 제곱근은 3)

#     if distance == num_jegob: # 4 흰색
#         count = (num*2)-1 #3

#     elif num_jegob < distance <= num_jegob + num: # 5, 6 노랑
#         count = (num*2)

#     elif (num_jegob + num) < distance: # 7,8 파랑
#         count = (num*2) + 1

#     elif distance < 4: # 1,2,3
#         count = distance

#     result.append(count) # [이동횟수,이동횟수,이동횟수]

# for x in result:
#     print(x)

# -----------------------------------------------------------------------
# 백준 4948번 베르트랑 공준
# import math
# import sys

# def num(num): # 소수 구하는 함수 3 5 7 11 ...
#     if num == 1:
#         return False
#     else :
#         for i in range(2,int(math.sqrt(num))+1) :
#             if num%i == 0:
#                 return False
#         return True

# all_list = list(range(2,246912)) # 문제에서 주어진 범위
# save_list=[]

# for i in all_list : # 주어진 범위 안의 소수들을 찾아서 저장해놓는다.
#     if num(i):
#         save_list.append(i)


# num = int(sys.stdin.readline())

# while num != 0:
#     count = 0
#     for i in save_list: # 저장된 소수들 중,
#         if num < i <= num*2:
#             count += 1
#     print(count)
#     num = int(sys.stdin.readline())

# -----------------------------------------------------------------------
# 백준 1436번 영화감독 숌

# n = int(input())
# count = 0
# six = 666

# while True :
#     if '666' in str(six): # 브루트포스(하나씩 더하여 값을 찾아감.)
#         count += 1
#     if count == n:
#         print(six)
#         break
#     six += 1

# -----------------------------------------------------------------------
# 백준 9184 신나는 함수실행

# import sys
# input = sys.stdin.readline

# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0: # 1~20의 범위
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)

#     if dp[a][b][c] :
#         return dp[a][b][c]

#     if a<b<c :
#         dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
#     else:
#         dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)

#     return dp[a][b][c]



# dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)] # a,b,c 각각의 값을 담는 배열
# while True:
#     a,b,c = map(int, input().split())
#     if a==-1 and b==-1 and c==-1:
#         break
#     print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c))) # 함수실행

# -----------------------------------------------------------------------
# 백준 9461 파도반수열
# 1. 1~100까지의 범위
# 2. 1,2,3은 111 이다
# 3. 4부터의 범위를 돌려서 값을 찾는다.

# a = [0 for i in range(101)] # 0부터 100의 범위
# a[1] = 1
# a[2] = 1
# a[3] = 1

# for i in range(0,98): # [1,1,1,2,2,3,4,5,7,9,12,16....] 하나씩 돌면서 리스트에 넣음.
#     a[i+3] = a[i] + a[i+1]

# n = int(input())
# for i in range(n):
#     m =int(input())
#     print(a[m]) # m번째 인덱스 값을 출력해라.

# -----------------------------------------------------------------------
# 백준 1149 RGB거리

# n = int(input())
# p = []
# for i in range(n):
#     p.append(list(map(int, input().split())))
# for i in range(1, len(p)):  # 두번째 집부터 최솟값을 구하고, 리스트에 넣어서 값을 바꾼다
#     p[i]1[0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0] # 빨간집
#     p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1] # 초록집
#     p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2] # 파란집
# print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))  # 두번째 집의 최솟값이 담긴 리스트와 세번째(마지막)집을 비교하여 최솟값을 출력한다.

# -----------------------------------------------------------------------
# 백준 1932 정수 삼각형
# n = int(input())
# t = []

# for i in range(n):
#     t.append(list(map(int, input().split())))
# k = 2
# for i in range(1, n): # i = 1,2,3,4
#     for j in range(k): # j = 0,1 / 0,1,2 / 0,1,2,3 / 0,1,2,3,4
#         if j == 0:
#             t[i][j] = t[i][j] + t[i - 1][j] # 맨 앞자리
#         elif i == j:
#             t[i][j] = t[i][j] + t[i - 1][j - 1] # 맨 뒷자리
#         else:
#             t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j] # 나머지(가운데)는 자기 기준으로 왼쪽,오른쪽과 비교하여 큰 값을 더한다.
#     k += 1
# print(max(t[n - 1]))

# -----------------------------------------------------------------------
# 백준 11047 동전 0
# n, k = map(int,input().split())
# coin = []
# count = 0

# for i in range(n):
#     coin.append(int(input()))

# for i in range(n-1,-1,-1): # 10,9,8,7 ... 카운트다운
#     if k == 0:
#         break # 반복문 탈출
#     if coin[i] > k :
#         continue # 반복문의 처음으로 돌아가라.
#     count += k // coin[i]
#     k %= coin[i] # k = k % coin[i]
# print(count)

# -----------------------------------------------------------------------
# 백준 11399 ATM

# n = int(input())
# time = list(map(int,input().split()))
# num = 0
# time.sort()

# for i in range(n): # 0 1 2 3 4
#     num += sum(time[:i+1]) 
# print(num)

# -----------------------------------------------------------------------
# 백준 1037 약수
# n = int(input())
# a = list(map(int,input().split()))

# a_max = max(a)
# a_min = min(a)

# print(a_max*a_min)

# -----------------------------------------------------------------------
# 백준 2609 최대공약수와 최소공배수

# a,b = map(int,input().split())

# def gcd(a,b): # 최대공약수 , 유클리드 호제법 , GCD(a,b)=GCD(b,a%b) b가 0이 될 때까지
#     if b == 0 :
#         return a # a의 값을 반환해라.
#     else :
#         return gcd(b,a%b)

# def lcm(a,b): # 최소공배수 LCM(a,b) = GCD*(a/GCD)*(b/GCD)
#     g = gcd(a,b)
#     return int(g*(a/g)*(b/g))

# print(gcd(a,b))
# print(lcm(a,b))

# -----------------------------------------------------------------------
# 벡준 1934 최소공배수

# n = int(input())

# def gcd(a,b):
#     if b == 0 :
#         return a
#     else : 
#         return gcd(b,a%b)

# def lcm(a,b):
#     g = gcd(a,b)
#     return int(g*(a/g)*(b/g))

# for i in range(n):
#     a,b = map(int,input().split())
#     print(lcm(a,b))

# -----------------------------------------------------------------------
# 백준 11050 이항 계수 1

# from math import factorial

# n,k = map(int,input().split())
# b = factorial(n)// (factorial(k)*(factorial(n-k)))
# print(b)



# <번외> factorial 함수 만들기 (5 = 5*4*3*2*1=120)

# def factorial(n):
#     num = 1
#     for i in range(1,n+1):
#         num *= i
#     return num

# -----------------------------------------------------------------------
# 백준 1010 다리놓기

# from math import factorial

# n = int(input())

# for i in range(n) :
#     k,n = map(int,input().split())
#     b = factorial(n)// (factorial(k)*(factorial(n-k)))
#     print(b)

# -----------------------------------------------------------------------
# 백준 10828 스택

# import sys

# n = int(sys.stdin.readline())
# stack = []

# for i in range(n):
#     command = sys.stdin.readline().split()

#     if command[0] == 'push':
#         stack.append(command[1])
#     elif command[0] == 'pop':
#         if len(stack) ==0:
#             print(-1)
#         else :
#             print(stack.pop())
#     elif command[0] == 'size':
#         print(len(stack))
#     elif command[0] == 'empty':
#         if len(stack) == 0 :
#             print(1)
#         else :
#             print(0)
#     elif command[0] == 'top':
#         if len(stack) == 0 :
#             print(-1)
#         else :
#             print(stack[-1])

# -----------------------------------------------------------------------
# 백준 10773 제로

