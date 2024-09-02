import sys
input = sys.stdin.readline

mod = 10007
n = int(input())  # 직사각형 길이 
D = [0] * (1001) 
D[1] = 1  # 길이가 2x1일 때 타일의 경우의 수
D[2] = 2  # 길이가 1x2일 때 타일의 경우의 수

for i in range(3, n+1):
    D[i] = (D[i-1] + D[i-2]) % mod 

print(D[n])