import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드, 엣지 개수
edges = []  # 엣지 정보 저장 리스트
dist = [sys.maxsize] * (n+1)  # 거리 리스트, 큰 수로 초기화 

# 엣지 데이터 저장 
for i in range(m):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만-포드 수행 
dist[1] = 0  # 출발 노드 0으로 설정 

for _ in range(n+1):
    for start, end, time in edges:
        if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
            dist[end] = dist[start] + time  # 업데이트 

mCycle = False  # 음수 사이클 여부 변수

for start, end, time in edges:
    if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
        mCycle = True  # 업데이트가 가능하면 음수 사이클이 존재 

if not mCycle:  # 음수 사이클이 아니면 
    for i in range(2, n+1):
        if dist[i] != sys.maxsize:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)  # 음수 사이클이면 -1 출력 