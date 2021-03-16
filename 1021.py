# 백준 1021 회전하는 큐

n, m = map(int,input().split())  # [10,3]
targets = list(map(int,input().split())) # [2,9,5]
queue = [ i for i in range(1, n+1)] # [1,2,3,4,5,6,7,8,9,10]
result = 0

for i in range(m):
    queue_len = len(queue) # 10
    index = queue.index(targets[i]) 2 = 1 / 5 = 4 / 9 = 8
    # print(index) # targets의 위치값 구하기

    if index < queue_len - index : # 구하고자 하는 위치가 앞쪽에 있는 경우 앞으로 이동이 유리하다
        while True : 
            if queue[0] == targets[i] :
                del queue[0]
                break
            else :
                queue.append(queue[0]) # 첫번째 요소를 맨 뒤에 추가하고, 첫번째 요소는 지워 이동한다.
                del queue[0]
                result += 1 # 이동횟수 + 1
    else : 
        while True : # 구하고자 하는 위치가 뒤쪽에 있는 경우 뒤로 이동이 유리하다
            if queue[0] == targets[i] :
                del queue[0]
                break
            else :
                queue.insert(0,queue[-1]) # 마지막 요소를 첫번째로 넣어주고 마지막 요소는 지운다.
                del queue[-1]
                result += 1 # 이동횟수 + 1
print(result)