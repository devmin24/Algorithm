# 백준 2606 바이러스
from sys import stdin
read = stdin.readline # 이걸 사용하면 인풋을 대입해줄 필요없이 직접 read를 쓰면 됨
dic={} # {1:{a,b}}
for i in range(int(read())): # 7
    dic[i+1] = set() # 인덱스는 0부터 시작이니까 +1 해줌
for j in range(int(read())): # 6
    a, b = map(int,read().split()) # [1,2][2,3][1,5][5,2][5,6][4,7]
    dic[a].add(b) #양방향 성질
    dic[b].add(a)

def bfs(start):
    queue = [start]
    while queue:
        for i in dic[queue.pop(0)]: # 큐(선입선출법) 첫번째꺼 지워주고 마지막에 넣어준다
            if i not in visited: # visited에 값이 없으면
                visited.append(i)
                queue.append(i)
visited = [] #[2,5,1,3,6]
bfs(1) # = start = 1
print(len(visited)-1) # 1은 숫주 그 자체이므로 감염된 컴퓨터 수를 구하기 위해 -1