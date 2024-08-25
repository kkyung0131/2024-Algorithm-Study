import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())  # 수 개수 
tree = [[] for _ in range(n+1)]  # 트리 데이터 저장 인접 리스트 

# 인접 리스트에 트리 데이터 저장 
for _ in range(0, n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
    
depth = [0] * (n+1)  # 각 노드의 깊이 저장 리스트 
parent = [0] * (n+1)  # 부모 노드 저장 리스트 
visited = [False] * (n+1)  # 방문 기록 리스트 

# BFS 구현
def BFS(node):
    queue = deque()  # 큐 자료구조 선언
    queue.append(node)  # 현재 노드 큐에 삽입
    visited[node] = True  # 방문 기록 
    level = 1  # 현재 노드에서 트리 깊이 
    now_size = 1  # 현재 깊이에서 트리 크기 
    cnt = 0  # 카운트 
    while queue:  # 큐가 빌 때까지 
        now_node = queue.popleft()  # 현재 노트 pop 
        for next in tree[now_node]:  # 인접 노드에 대해서 
            if not visited[next]:  # 미방문 노드이면 
                visited[next] = True  # 방문 기록
                queue.append(next)  # 큐에 삽입 
                parent[next] = now_node  # 부모 노드 저장 
                depth[next] = level  # 노드 깊이 저장 
        cnt += 1  # 카운트 1 증가 
        if cnt == now_size:  # 카운트와 현재 트리 크기가 같으면 
            cnt = 0  # 카운트 초기화 
            now_size = len(queue)
            level += 1  # 깊이 1 증가 

BFS(1)

# LCA 구현 
def LCA(a,b):
    if depth[a] < depth[b]:  # a 깊이가 b보다 작으면
        temp = a 
        a = b 
        b = temp  # a와 b swap 
    
    while depth[a] != depth[b]:  # 두 노드 깊이가 같아질 때까지 
        a = parent[a]  # 부모 노드 변경 
    
    while a != b:  # 공통 조상 찾기 
        a = parent[a]
        b = parent[b]
    
    return a 
    
m = int(input())  # 질의 개수 

for _ in range(m):
    a, b = map(int, input().split())
    print(str(LCA(a,b)))
    print("\n")