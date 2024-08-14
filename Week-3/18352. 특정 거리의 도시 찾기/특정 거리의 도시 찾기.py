import sys
from collections import deque
input = sys.stdin.readline

# 노드 개수, 엣지 개수, 목표 거리, 시작점 
n, m, k, x = map(int, input().split())  
A = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1)

# BFS 함수 구현
def BFS(v):
    queue = deque()  # 큐 자료구조 선언
    queue.append(v)  # 시작점 삽입
    visited[v] += 1  # 방문 기록
    while queue:  # 큐에 값이 있는 동안
        now = queue.popleft()  # 현재 노드 pop 
        for i in A[now]:  # 인접 노드 중
            if visited[i]==-1:  # 미방문 노드에 대해
                visited[i] = visited[now] + 1  # 방문 기록 업데이트 
                queue.append(i)  # 큐에 삽입 

for _ in range(m):
    s, e = map(int, input().split())  # 시작 인덱스, 종료 인덱스 
    A[s].append(e)  # 방향 그래프 

BFS(x)  # 탐색

for i in range(n+1):
    if visited[i] == k:  # 방문 거리가 k이면 
        answer.append(i)  # 정답 리스트에 더하기 

if not answer:
    print(-1)
else:
    answer.sort()  # 정렬 후 
    for i in answer:
        print(i)  # 순차적으로 출력 