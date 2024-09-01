import sys
input = sys.stdin.readline

n = int(input())  # 연산 횟수
D = [0] * (n+1)  # DP 테이블
D[1] = 0  # 1일 때 연산 불필요

# 바텀-업 방식
for i in range(2, n+1):
    D[i] = D[i-1] + 1  # 1 빼는 연산 
    if i % 2 == 0:  # 2의 배수이면
        D[i] = min(D[i], D[i//2]+1)
    if i % 3 == 0:  # 3의 배수이면 
        D[i] = min(D[i], D[i//3]+1)

print(D[n])