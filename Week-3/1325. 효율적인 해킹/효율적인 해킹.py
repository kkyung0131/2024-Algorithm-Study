import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드 개수, 엣지 개수 
A = [[] for _ in range(n+1)]  # 인접 리스트 
answer = [0] * (n+1)  # 정답 리스트 

# BFS 구현
def BFS(v):
    queue = deque()  # 큐 자료구조 선언
    queue.append(v)  # 시작점 큐에 삽입
    visited[v] = True  # 방문 기록 
    while queue:
        now = queue.popleft()  # 현재 노드를 pop 
        for i in A[now]:
            if not visited[i]:  # 미방문 노드에 대해 
                visited[i] = True  # 방문 기록하고 
                answer[i] += 1  # 정답 리스트값 증가 
                queue.append(i)  # 큐에 삽입 

# 인접 리스트에 데이터 저장
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)

# 모든 노드에서 BFS 실행
for i in range(1, n+1):
    visited = [False] * (n+1)  # 방문 기록 리스트 초기화
    BFS(i)

maxVal = 0
for i in range(1, n+1):
    maxVal = max(maxVal, answer[i])

# 정답 출력 
for i in range(1, n+1):
    if maxVal == answer[i]:
        print(i, end=' ')