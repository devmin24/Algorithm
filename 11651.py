num = int(input())
a = []

for i in range(num):
    [x,y] = map(int, input().split()) # 입력값을 공백을 제외하여 정수로 리스트 [x,y]에 넣어준다
    rev = [y,x] # x,y로 받은 값을 뒤집어줌 (y 기준으로 정렬하기 위해)
    a.append(rev) # 뒤집어준 값을 a리스트에 넣어준다
b = sorted(a) # a에 들어간 요소들을 정렬하여 b에 넣어준다
for i in range(num) : # x,y로 출력하기 위해 다시 순서를 뒤집어서 출력해준다.
    print(b[i][1],b[i][0])