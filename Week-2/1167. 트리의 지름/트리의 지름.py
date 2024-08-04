import sys
input = sys.stdin.readline

from collections import deque

n = int(input())  # 노드 개수
graph = [[] for _ in range(n+1)]  # 인접 리스트

# 데이터 저장 - (노드, 가중치) 함께 저장
for _ in range(n):
    data = list(map(int, input().split()))
    index = 0
    s = data[index]
    index += 1 
    while True:
        e = data[index]
        if e == -1:
            break
        v = data[index+1]
        graph[s].append((e,v))
        index += 2 
        
# BFS 구현 
def BFS(v):
    queue = deque()
    queue.append(v)  # 시작점 삽입
    visited[v] = True  # 방문 기록 
    while queue:
        now = queue.popleft()  # 현재 노드 pop
        for i in graph[now]:  # 인접한 노드 중 
            if not visited[i[0]]:  # 미방문 노드 
                visited[i[0]] = True  # 방문 기록 
                queue.append(i[0])  # 삽입 
                distance[i[0]] = distance[now] + i[1]  # 거리 리스트 업데이트 

# 방문 기록, 거리 리스트 초기화 
visited = [False] * (n+1)
distance = [0] * (n+1)

BFS(1)

maximum = 1
# 가장 큰 값의 노드를 시작점으로 재설정 
for i in range(2, n+1):
    if distance[maximum] < distance[i]:
        maximum = i 

# 방문 기록, 거리 리스트 초기화 
visited = [False] * (n+1)
distance = [0] * (n+1)

BFS(maximum)
print(max(distance))  # 최댓값을 정답으로 출력