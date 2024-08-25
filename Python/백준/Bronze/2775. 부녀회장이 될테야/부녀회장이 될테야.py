import sys 
input = sys.stdin.readline

D = [[0 for j in range(15)] for i in range(15)]

# DP 리스트 초기화
for i in range(15):
    D[i][1] = 1  # i층 1호는 항상 1의 값 
    D[0][i] = i  # 0층 i호는 i의 값
    
for i in range(1,15):
    for j in range(2,15):
        D[i][j] = D[i][j-1] + D[i-1][j]  # 점화식 
        
t = int(input())  # 테스트 케이스 

for i in range(0, t): 
    k = int(input())  # 층 수 
    n = int(input())  # 호 수 
    print(D[k][n])