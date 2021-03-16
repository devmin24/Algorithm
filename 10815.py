# 백준 10815 숫자카드

n = int(input())
num_card = list(map(int,input().split()))
m = int(input())
nums = list(map(int,input().split()))

num_card.sort()

for i in range(m) :
    low, high = 0, n-1
    while low <= high :
        mid = (low+high)//2
        if num_card[mid] == nums[i]:
            print(1,end=" ")
            break
        elif num_card[mid] < nums[i]:
            low = mid+1
        else:
            high = mid-1
        if low > high:
            print(0,end=" ")
            break