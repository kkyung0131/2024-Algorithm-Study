import sys
#sys.setrecursionlimit(10*6)  # 최대 재귀 깊이 설정정
input = sys.stdin.readline

n, m = map(int, input().split())  # 노드의 개수, 엣지의 개수 

graph = [[] for _ in range(n+1)]  # 인접 리스트 선언, 인덱스 그대로를 정점 번호로 사용 가능  가능 
visited = [False] * (n+1)  # 방문 기록 리스트 선언 
cnt = 0  # 연결 요소 개수 

# DFS 구현
def DFS(v):
    visited[v] = True  # 방문 기록
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않았다면 탐색
            DFS(i)  # 스택 성질을 가지고 있는 재귀 함수

# 인접 리스트 구성 
for _ in range(m):  # 엣지의 개수만큼 
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)  # 양방향 엣지 

for i in range(1, n+1):
    if not visited[i]:  # 방문하지 않은 노드가 존재한다면
        cnt += 1  # 연결요소 증가
        DFS(i)  # DFS 탐색 또 시작

print(cnt)