import sys
input = sys.stdin.readline

D = [[0 for j in range(31)] for i in range(31)]  # DP 리스트 

# DP 리스트 초기화
for i in range(0, 31):
    D[i][1] = i 
    D[i][0] = 1 
    D[i][i] = 1 

for i in range(2,31):
    for j in range(1,i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]  # 점화식 

t = int(input())  # 테스트 케이스 

for i in range(0, t):
    n, m = map(int, input().split())
    print(D[m][n])