import sys
input = sys.stdin.readline

# 리스트 크기와 질의 수 입력
n, m = map(int, input().split())  
A = [[0] * (n+1)]  # 원본 리스트 선언
D = [[0] * (n+1) for _ in range(n+1)]  # 합 배열 선언

# A 리스트 생성
for i in range(n):
    # 리스트 앞에 0을 추가 → 인덱스와 순서를 동일하게 하기 위함
    A_row = [0] + [int(x) for x in input().split()]  
    A.append(A_row)
    
# D 합 배열 생성
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# 구간 합 배열 
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
