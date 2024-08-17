import sys
input = sys.stdin.readline

from queue import PriorityQueue

n = int(input())  # 도시 개수
m = int(input())  # 버스 개수 
A = [[] for _ in range(n+1)]  # 인접 리스트
dist = [sys.maxsize] * (n+1)  # 큰 수로 초기화한 거리 리스트 
visit = [False] * (n+1)  # 방문 기록 리스트 

# 인접 리스트에 데이터 저장 
for _ in range(m):
    s, e, w = map(int, input().split())
    A[s].append((e,w))

start, end = map(int, input().split())  # 시작, 도착 노드 

# 다익스트라 함수 구현
def dijkstra(start, end):
    pq = PriorityQueue()  # 우선순위 큐 선언 
    pq.put((0, start))  # 시작 노드 삽입 
    dist[start] = 0  # 거리 0으로 설정 
    while not pq.empty():
        nowNode = pq.get()  # 현재 노드를 가져와서 
        now = nowNode[1]
        if not visit[now]:  # 미방문이면 
            visit[now] = True  # 방문 기록 
            for next, value in A[now]:
                if not visit[next] and dist[next] > dist[now] + value:
                    dist[next] = dist[now] + value  # 최단거리 업데이트
                    pq.put((dist[next], next))  # 큐에 삽입 
    return dist[end]  # 도착 노드의 최단 거리 출력 

print(dijkstra(start, end))