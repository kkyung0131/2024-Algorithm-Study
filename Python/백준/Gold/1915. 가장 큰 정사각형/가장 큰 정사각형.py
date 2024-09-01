import sys
input = sys.stdin.readline

D = [[0 for j in range(1001)] for i in range(1001)]  
n, m = map(int, input().split())  # 세로, 가로 길이 
mymax = 0  # 최댓값 저장할 변수 

for i in range(n):
    num = list(input())  # 데이터를 한 줄씩 저장하는 리스트 
    for j in range(0, m):
        D[i][j] = int(num[j])
        if (D[i][j] == 1) and (j > 0) and (i > 0):
            D[i][j] = min(D[i-1][j-1], D[i-1][j], D[i][j-1]) + D[i][j]  # 점화식 
        if mymax < D[i][j]:
            mymax = D[i][j]
        
print(mymax**2)