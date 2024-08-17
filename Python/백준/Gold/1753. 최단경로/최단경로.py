import sys
from queue import PriorityQueue

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())  # 노드, 엣지 개수 
k = int(input())  # 출발 노드 
distance = [INF] * (V+1)  # 거리 저장 리스트, 큰 값으로 초기화
visited = [False] * (V+1)  # 방문 기록 리스트 
myList = [[] for _ in range(V+1)]  # 인접 리스트 
q = PriorityQueue()  # 우선순위 큐 선언 

# 인접 리스트 저장 
for _ in range(E):
    u, v, w = map(int, input().split())  # u → v (가중치 w)
    myList[u].append((v,w))

q.put((0,k))  # 출발 노드를 우선순위 큐에 추가 
distance[k] = 0  # 거리 리스트에 출발 노드 값을 0으로 설정 

# 다익스트라
while not q.empty():
    dist, now = q.get()  # 현재 노드 가져오기 
    
    if visited[now]:  # 방문했다면 다음으로 넘어가기
        continue
    visited[now] = True  # 방문 기록 
    
    for next, value in myList[now]:  # 현재 선택 노드의 엣지 개수만큼 
        if distance[next] > distance[now] + value:  # 최소 거리로 업데이트 
            distance[next] = distance[now] + value 
            q.put((distance[next], next))
            
for i in range(1, V+1):
   print("INF" if distance[i] == INF else distance[i])
   