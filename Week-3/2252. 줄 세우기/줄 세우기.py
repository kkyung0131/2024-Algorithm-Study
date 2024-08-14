import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())  # 학생 수, 비교 횟수
A = [[] for _ in range(n+1)]  # 인접 리스트
indegree = [0] * (n+1)  # 진입 차수 리스트 

for i in range(m):
    s, e = map(int, input().split())
    A[s].append(e)  # 인접 리스트에 데이터 저장 
    indegree[e] += 1  # 진입 차수 데이터 저장 
    
queue = deque()  # 큐 자료구조 선언

for i in range(1, n+1):
    if indegree[i] == 0:  # 진입 차수 리스트 값이 0이면
        queue.append(i)  # 큐에 삽입

# 위상 정렬 수행 
while queue:
    now = queue.popleft()  # 현재 노드 pop
    print(now, end=' ')  # 공백을 두고 출력 
    for next in A[now]:  # 현재 노드에서 갈 수 있는 노드 개수 
        indegree[next] -= 1  # 진입 차수 리스트값 1 감소 
        if indegree[next] == 0:  # 타깃 노드의 진입 차수가 0이면: 
            queue.append(next)  # 큐에 타깃 노드 추가