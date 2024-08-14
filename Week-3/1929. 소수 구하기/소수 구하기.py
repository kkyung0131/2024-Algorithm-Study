import math
import sys
input = sys.stdin.readline

m, n = map(int, input().split())  # 시작 수, 종료 수
A = [0] * (n+1)  # n+1 크기의 배열 생성

# A 리스트 값을 각각의 인덱스 값으로 초기화
for i in range(2,n+1): 
    A[i] = i

# 2부터 n의 제곱근까지만 탐색 
for i in range(2, int(math.sqrt(n))+1):
    if A[i]==0:  # 소수가 아니면 패스
        continue
    for j in range(i+i, n+1, i):
        A[j]=0  # 배수 지우기 

# m 이상 n 이하의 소수 출력
for i in range(m, n+1):
    if A[i] != 0:
        print(A[i])