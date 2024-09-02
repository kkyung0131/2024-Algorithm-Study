import sys
input = sys.stdin.readline

mod = 1000000000  # 나머지 연산
n = int(input())  # 수 길이
D = [[0 for j in range(11)] for i in range(n+1)]

# 길이가 1일 때 만드는 높이 h로 끝나는 계단 수의 모든 경우의 수는 1 
for i in range(1, 10):
    D[1][i] = 1 

for i in range(2, n+1):
    D[i][0] = D[i-1][1]  # 높이가 0일 때 
    D[i][9] = D[i-1][8]  # 높이가 9일 때 
    for j in range(1,9):  # 높이가 1~8일 때
        D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % mod
    
mysum = 0

for i in range(10):
    mysum = (mysum + D[n][i]) % mod 

print(mysum)