# 백준 1316 그룹 단어 체커

n = int(input()) 

group_word = 0
for _ in range(n):
    word = input()
    error = 0
    for index in range(len(word)-1): #인덱스 범위 생성 0부터 len(word)-1
        if word[index] != word[index+1]: #연속된 문자가 다를 때
            new_word = word[index+1:] # 현재 문자의 다음부터 문자열을 새로운 변수에 저장한다
            if new_word.count(word[index]) > 0: # 저장된 변수에 현재 문자가 하나라도 있으면
                error += 1 # 그룹문자가 아니기때문에 error +=1 을 해준다
    if error == 0: # error가 없으면 그룹문자이다. (연속된 문자는 에러가 없다.)
        group_word += 1
print(group_word)