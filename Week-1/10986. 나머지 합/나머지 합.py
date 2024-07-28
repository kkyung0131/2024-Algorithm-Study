import sys
input = sys.stdin.readline

# 수열의 개수, 나누는 수 입력 받기
n, m = map(int, input().split())
A = list(map(int, input().split()))  # 원본 수열 입력 받기
S = [0] * n  # 합 배열
C = [0] * m  # 나머지 인덱스 카운트 리스트
S[0] = A[0]
answer = 0  # 정답 변수 선언

# 합 배열 저장
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 합 배열을 0으로 나눈 나머지 저장
for i in range(n):
    remainder = S[i] % m  # 나머지 연산
    if remainder == 0:  
        answer += 1  # 0일 때 정답 더하기
    C[remainder] += 1  # 나머지가 같은 인덱스 개수 값 증가

for i in range(m):
    if C[i] > 1:  
        answer += (C[i] * (C[i]-1) // 2)  # // 연산으로 정수형 출력 

print(answer)
