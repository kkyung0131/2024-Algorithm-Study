import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 도시 수
m = int(input())  # 도로 수
A = [[] for _ in range(n+1)]  # 도시 인접 리스트 
rA = [[] for _ in range(n+1)]  #  역방향 A 리스트 
indegree = [0] * (n+1)  # 진입 차수 리스트 

for i in range(m):
    s, e, v = map(int, input().split()) 
    A[s].append((e,v))  # 인접 리스트에 데이터 저장 
    rA[e].append((s,v))  # 역방향 엣지 정보 저장 
    indegree[e] += 1  # 진입 차수 리스트 저장 

start, end = map(int, input().split())  # 출발 도시, 도착 도시 

queue = deque()  # 큐 선언 
queue.append(start)  # 시작 도시 삽입
result = [0] * (n+1)  # 결과 리스트 초기화 

# 위상 정렬 
while queue:
    now = queue.popleft()  # 현재 노드 pop 
    for next in A[now]:  # 인접 노드에 대해서 
        indegree[next[0]] -= 1  # 진입 차수 1 감소 
        result[next[0]] = max(result[next[0]], result[now]+next[1])  # 결과 업데이트 
        if indegree[next[0]] == 0:  # 진입 차수가 0이면 
            queue.append(next[0])  # 큐에 삽입 

resultCnt = 0  # 1분도 쉬지 않고 달려야 하는 도로의 수 
visited = [False] * (n+1)  # 방문 기록 리스트 
queue.clear()  # 큐 초기화 
queue.append(end)  # 도착 도시 삽입 
visited[end] = True

# 위상 정렬 reverse 
while queue:
    now = queue.popleft() 
    for next in rA[now]:
        if result[next[0]] + next[1] == result[now]:  # 1분도 쉬지 않는 도로이면 
            resultCnt += 1 
            if not visited[next[0]]:  # 미방문 노드에 한해 
                visited[next[0]] = True  # 방문 기록 
                queue.append(next[0])  # 큐에 삽입 

# 결과 출력 
print(result[end])
print(resultCnt)