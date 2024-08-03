import sys
sys.setrecursionlimit(10*4)
input = sys.stdin.readline 

n, m = map(int, input().split())
arrive = False
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v, depth):  # 현재 노드, 깊이
    global arrive  # 전역변수 
    
    if depth == 5:  # 깊이가 5이면 종료
        arrive = True  # 도착
        return 
    
    visited[v] = True  # 방문 기록
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드에 대해서
            DFS(i, depth+1)  # 깊이 증가
    visited[v] = False

for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)  # 양방향 그래프
    graph[e].append(s)
    
for i in range(n):
    DFS(i, 1)  # 노드마다 DFS 수행
    if arrive:  # 도착하면
        break  # 반복문 종료 

if arrive: 
    print(1)  # 도착하면 1 출력
else:
    print(0)  # 도착하지 못하면 0 출력 