# 백준 1436번 영화감독 숌

n = int(input())
count = 0
six = 666

while True :
    if '666' in str(six): # 브루트포스(하나씩 더하여 값을 찾아감.)
        count += 1
    if count == n:
        print(six)
        break
    six += 1
