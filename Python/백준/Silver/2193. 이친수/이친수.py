import sys
input = sys.stdin.readline

n = int(input())  # 자릿수
D = [[0 for j in range(2)] for i in range(n+1)]  # 점화식 테이블
D[1][1] = 1  # 1은 이친수
D[1][0] = 0  # 0으로 시작하는 1자리 이친수 없음 

for i in range(2,n+1):
    D[i][0] = D[i-1][1] + D[i-1][0]
    D[i][1] = D[i-1][0]

print(D[n][0] + D[n][1])