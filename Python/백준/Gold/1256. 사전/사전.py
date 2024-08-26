import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # a문자 개수, z문자 개수, 순번 
D = [[0 for j in range(202)] for i in range(202)]  # 조합 경우의 수 저장 테이블

# 조합 테이블 생성
for i in range(201):
    for j in range(i+1):
        if j==0 or j==i:
            D[i][j] = 1 
        else:
            D[i][j] = D[i-1][j] + D[i-1][j-1]  # 점화식 
            if D[i][j] > 1000000000:  # 범위를 벗어나면 
                D[i][j] = 1000000001  # 최댓값 저장 

if D[n+m][m] < k:  # 불가능한 k이면 
    print(-1)
else:
    while not (n==0 and m==0):
        if D[n-1+m][m] >= k:
            print('a', end='')
            n -= 1 
        else:
            print('z', end='')
            k -= D[n-1+m][m]
            m -= 1