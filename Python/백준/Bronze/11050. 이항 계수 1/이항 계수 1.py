import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 총 개수, 선택 수 
D = [[0 for j in range(n+1)] for i in range(n+1)]  # DP 리스트 

# DP 리스트 초기화 
for i in range(0, n+1):
    D[i][1] = i  # i개에서 1개를 선택하는 경우의 수 i개 
    D[i][0] = 1  # i개에서 1개도 선택하지 않는 경우의 수 1개 
    D[i][i] = 1  # i개에서 모두 선택하는 경우의 수 1개 
    
# 조합 기본 점화식 계산 
for i in range(2, n+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]

print(D[n][k])