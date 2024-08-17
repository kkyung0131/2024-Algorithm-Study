import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 유저 수, 친구 관계 수
dist = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]  # 인접행렬 

# 인접 행렬 중 같은 노드의 값을 0으로 초기화 
for i in range(1,n+1):
    dist[i][i] = 0 

# 인접 행렬 데이터 저장 
for i in range(m):
    s, e = map(int, input().split())
    dist[s][e] = 1
    dist[e][s] = 1  # 양방향 엣지, 가중치 1 

# 플로이드-워셜
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

minimum = sys.maxsize  # 큰 수로 초기화 
answer = -1  # 정답 변수 

for i in range(1, n+1):
    temp = 0 
    for j in range(1, n+1):
        temp += dist[i][j]  # 행별로 값 합치기 
    if minimum > temp:  # 가장 작은 케빈 베이컨 수를 지닌 i를 찾아서 
        minimum = temp
        answer = i  # 결과 저장 

print(answer)