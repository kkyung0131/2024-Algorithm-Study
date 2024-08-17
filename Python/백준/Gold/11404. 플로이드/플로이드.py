import sys
input = sys.stdin.readline

n = int(input())  # 도시 개수
m = int(input())  # 노선 개수 
dist = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]  # 인접 행렬

# 인접 행렬 중 값이 같은 노드는 0으로 초기화
for i in range(1, n+1):
    dist[i][i] = 0

# 인접 행렬 데이터 저장 
for i in range(m):
    s, e, v = map(int, input().split())
    if dist[s][e] > v:  # 최단 거리로 저장 
        dist[s][e] = v 

# 플로이드-워셜 
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]  # 값 업데이트 

# 정답 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == sys.maxsize:
            print(0, end=' ')  # 도착할 수 없는 경로 
        else:
            print(dist[i][j], end=' ')
    print()