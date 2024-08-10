import sys
input = sys.stdin.readline

answer = 0  # 정답 변수
A = list(map(str, input().split('-')))  # '-' 기준으로 split한 문자데이터 저장

# 각 string의 수를 더하는 함수
def stringSum(i):
    result = 0  # 합 
    temp = str(i).split("+")  # 현재 string을 '+' 기준으로 split 
    for i in temp:  
        result += int(i)  # split된 값을 integer로 변환 후 더하기 
    return result 

for i in range(len(A)):
    temp = stringSum(A[i])  # 더하기 함수 수행 후
    if i == 0:  # 맨 처음 수는 
        answer += temp  # 더해주고 
    else:  # 그 다음 수부터는 
        answer -= temp  # 빼주기 

print(answer)  # 결과 출력 