import sys
input = sys.stdin.readline

n = int(input())  # 수 개수
A = [0] * n  # 수 저장 리스트 

# 입력 데이터를 리스트에 저장 
for i in range(n):
    A[i] = int(input())

for i in range(n-1):  # 0~n-1
    for j in range(n-1-i):  # 0~n-1-i 
        if A[j] > A[j+1]:  # 인접한 두 수 중 왼쪽이 더 크면
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp  # swap 

# 정렬 결과 출력 
for i in range(n):
    print(A[i])
