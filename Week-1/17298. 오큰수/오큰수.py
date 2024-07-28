import sys
input = sys.stdin.readline

n = int(input())  # 수열 개수
A = list(map(int, input().split()))  # 수열 리스트
ans = [-1] * n  # 정답 리스트를 -1로 초기화
myStack = []  # 스택 선언

for i in range(n):
    # top(myStack[-1])보다 현재 수열(A[i])이 더 크면
    while myStack and A[myStack[-1]] < A[i]:
        # 현재 수열값이 오큰수가 됨, 해당하는 인덱스에 추가
        ans[myStack.pop()] = A[i] 
    myStack.append(i)  # 인덱스 하나 추가

result = ' '.join(map(str, ans))  # 공백으로 나누어 출력 
print(result)
