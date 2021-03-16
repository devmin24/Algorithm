# 백준 18258 큐 2
import sys
from collections import deque
n = int(sys.stdin.readline())
dq = deque([])

for i in range(n):
    m = sys.stdin.readline().split()
    if m[0] == 'push':
        dq.append(m[1])
    elif m[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else :
            print(dq.popleft())
    elif m[0] == 'size':
        print(len(dq))
    elif m[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else :
            print(0)
    elif m[0] == 'front':
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])
    elif m[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else :
            print(dq[-1])
