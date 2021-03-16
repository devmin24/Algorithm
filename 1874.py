n = int(input())
count = 0
stack = []
result = []
no = True

for i in range(0,n) :
    x = int(input())

    while count < x : 
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == x :
        stack.pop()
        result.append("-")
    else : 
        no = False
        break

if no == False : 
    print("No")
else : 
    print("\n".join(result)) #리스트의 요소들을 줄바꿈으로 표현하는 법