n, m = map(int,input().split()) # n = 나무의 수 m = 필요한 나무의 길이
tree = list(map(int,input().split())) # 그루 당 나무의 길이 리스트

def h(m,tree) :
    start = 1
    end = max(tree) # 리스트 안의 나무에서 제일 키 큰 나무의 길이
    
    while start <= end : # start가 end보다 작아지면 범위가 []없기 때문에 끝난다.
        leng = 0 # 자른 나무 길이의 합을 담아둘 변수
        mid = (start + end) // 2 # start ~ end 의 중간값

        for i in tree :  # 일단 잘라보기
            if i >= mid :  # 중간값보다 한 그루의 나무가 길이가 크다면
                leng += i - mid # 잘라서 leng에 넣자

        if leng >= m : # leng(자른나무)가 m(필요한 나무의 길이)보다 크다면,
            start = mid + 1 # 시작점을 조정하여 범위를 줄이자 (더 높이 잘라야 덜 자를수 있기 때문)
        else : 
            end = mid - 1 # m보다 적게 잘랐다면 end 값을 줄여서 높이의 범위를 낮추자
    return end # 다 돌면 end를 변환해라.

print(h(m,tree)) # 함수를 실행하면 end만 남아 높이가 출력된다.