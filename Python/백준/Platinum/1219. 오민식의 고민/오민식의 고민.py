import sys
input = sys.stdin.readline

n, start, end, m = map(int, input().split())  # 노드 개수, 시작 도시, 종료 도시, 엣지 개수 
edges = []  # 엣지 리스트
dist = [-sys.maxsize] * n  # 최단거리 리스트 충분히 작은 수로 초기화

# 엣지 리스트 저장
for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s,e,w))

money = list(map(int, input().split()))  # 각 도시에서 버는 수입 저장 

# 변형된 벨만-포드 수행 
dist[start] = money[start]  # 출발 초기화 

for i in range(n+101):
    for s, e, w in edges:
        if dist[s] == -sys.maxsize:  # 미방문노드면
            continue  # pass 
        elif dist[s] == sys.maxsize:
            dist[e] = sys.maxsize 
        elif dist[e] < dist[s] + money[e] - w:  # 더 많은 돈을 벌 수 있는 경로가 있으면 
            dist[e] = dist[s] + money[e] - w  # 업데이트
            if i >= n-1:
                dist[e] = sys.maxsize 
                
if dist[end] == -sys.maxsize:  # 도착 불가능 
    print('gg')
elif dist[end] == sys.maxsize:  # 양수 사이클
    print("Gee")
else:
    print(dist[end])