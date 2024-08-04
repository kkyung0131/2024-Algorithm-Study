import sys
input = sys.stdin.readline

from collections import deque  # 큐 자료구조는 덱으로 구현 
n, m, start = map(int, input().split())  # 노드 개수, 엣지 개수, 시작점
graph = [[] for _ in range(n+1)]  # 인덱스 번호 = 노드 숫자

# graph에 데이터 저장
for _ in range(m):
    s, e = map(int, input().split())
    # 양방향 엣지
    graph[s].append(e)
    graph[e].append(s)

# 번호가 작은 것을 먼저 방문하기 위해 오름차순 정렬
for i in range(n+1):
    graph[i].sort()  # O(nlogn)

# DFS 구현
def DFS(v):
    print(v, end=' ')  # 탐색 결과를 공백을 두고 출력
    visited[v] = True  # 방문 기록 
    for i in graph[v]:  # 인접 노드
        if not visited[i]:  # 미방문 노드에 한해서
            DFS(i)  # 재귀함수 호출 

# BFS 구현
def BFS(v):
    queue = deque()  # 덱 자료구조 선언
    queue.append(v)  # 큐에 시작점 삽입 
    visited[v] = True  # 방문 기록 
    while queue:
        now = queue.popleft()  # 현재노드 pop
        print(now, end=' ')  # 탐색 결과를 공백울 두고 출력 
        for i in graph[now]:  # 인접 노드 
            if not visited[i]:  # 미방문 노드에 한해서 
                visited[i] = True  # 방문을 기록하고 
                queue.append(i)  # 큐에 삽입 

visited = [False] * (n+1)  # 방문 기록 리스트 초기화
DFS(start)  # 깊이 우선 탐색 결과 
print()

visited = [False] * (n+1)  # 방문 기록 리스트 초기화
BFS(start)  # 너비 우선 탐색 결과 