import sys
import heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 노드, 엣지, 몇 번째 최단경로
A = [[] for _ in range(n+1)]  # 인접 리스트 
dist = [[sys.maxsize]*k for _ in range(n+1)]  # 거리 리스트 

# 인접 리스트 저장 
for _ in range(m):
    s, e, w = map(int, input().split())
    A[s].append((e,w))
    
pq = [(0,1)]  # 가중치, 노드 순서로 저장 
dist[1][0] = 0  # 시작 노드 최단거리 0으로 설정 

while pq:
    cont, node = heapq.heappop(pq)
    for nNode, nCost in A[node]:
        sCost = cont + nCost  # 총 거리 = 현재 노드 거리 + 엣지 가중치 
        if dist[nNode][k-1] > sCost:
            dist[nNode][k-1] = sCost  # 거리 업데이트
            dist[nNode].sort()  # 정렬 
            heapq.heappush(pq, [sCost, nNode])  # 새 데이터 추가 
             
for i in range(1, n+1):
    if dist[i][k-1] == sys.maxsize:  # k번째 거리가 없으면 
        print(-1)  # -1 출력 
    else:
        print(dist[i][k-1])