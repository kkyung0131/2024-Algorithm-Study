import sys
input = sys.stdin.readline

n = int(input())  # 수열 개수
A = [0] * n  # 수열 리스트 초기화

# 수열 리스트 하나씩 채우기
for i in range(n):
    A[i] = int(input())

stack = []  # 스택 초기화 
num = 1  # 자연수 초기화 
result = True 
answer = ""  # 출력값

for i in range(n):
    value = A[i]  # 현재 수열값 
    if value >= num:  # 현재 수열값이 자연수보다 크거나 같으면
        while value >= num:  # 그동안
            stack.append(num)  # 자연수 오름차순으로 추가
            num += 1 
            answer += "+\n"  # + 저장 
        stack.pop()  # 현재 수열값이 자연수보다 작아지면 하나 꺼내기
        answer += "-\n"  # - 저장 
    else:  # 현재 수열값이 자연수보다 작으면 
        n = stack.pop()  
        if n > value:  # 스택 맨 위의 수가 현재 수열값보다 크면 
            print("NO")  # 출력 불가 
            result = False  
            break
        else:
            answer += "-\n"  # - 저장 

if result:  # NO가 출력된 적이 없으면
    print(answer)  # 결과 출력 