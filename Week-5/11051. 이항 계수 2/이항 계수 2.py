import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 총 개수, 선택 수 
D = [[0 for j in range(n+1)] for i in range(n+1)]  # DP 리스트 

# DP 리스트 초기화 
for i in range(0, n+1):
    D[i][1] = i
    D[i][0] = 1 
    D[i][i] = 1 

for i in range(2, n+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]  # 점화식 
        D[i][j] = D[i][j] % 10007  # 나머지 연산 
    
print(D[n][k])