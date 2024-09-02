import sys
input = sys.stdin.readline

n = int(input())  # 수열 크기 
A = list(map(int, input().split()))  # 수열 데이터 저장 리스트

# 왼쪽에서 오른쪽으로 index를 포함한 최대 연속 합 구하기 
L = [0] * n 
L[0] = A[0]
result = L[0]

for i in range(1, n):
    L[i] = max(A[i], L[i-1]+A[i])  # 왼쪽 합 리스트 저장 
    result = max(result, L[i])  # 제거하지 않았을 때 기본 최댓값 저장

# 오른쪽에서 왼쪽으로 index를 포함한 최대 연속 합 구하기 
R = [0] * n 
R[n-1] = A[n-1]

for i in range(n-2, -1, -1):
    R[i] = max(A[i], R[i+1] + A[i])  # 오른쪽 합 리스트 저장 

for i in range(1, n-1):
    temp = L[i-1] + R[i+1]
    result = max(result, temp)

print(result)