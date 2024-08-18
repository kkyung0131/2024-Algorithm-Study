import sys
input = sys.stdin.readline

n = int(input())  # 인접 행렬 크기 
dist = [[0 for j in range(n)] for i in range(n)]  # 인접 행렬 

# 인접 행렬 데이터 저장
for i in range(n):
    dist[i] = list(map(int, input().split()))
    
# 플로이드-워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            # 가능 경로 탐색 
            if dist[i][k] == 1 and dist[k][j]==1:
                dist[i][j] = 1  

# dist 출력
for i in range(n):
    for j in range(n):
        print(dist[i][j], end=' ')
    print()