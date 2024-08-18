import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())  # 노드 개수
visited = [False] * (n+1)  # 방문 기록 리스트 
tree = [[] for _ in range(n+1)]  # 트리 인접 리스트 
answer = [0] * (n+1)  # 부모 노드 정답 리스트 

# 트리 데이터 저장
for _ in range(1,n):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)
    
# DFS 구현
def DFS(v):
    visited[v] = True  # 방문 기록 
    for i in tree[v]:  # 인접 노드 중에서
        if not visited[i]:  # 미방문 노드이면 
            answer[i] = v  # 부모 노드로 현재 노드를 저장 
            DFS(i)

DFS(1)  # 부모 노드부터 DFS 시작 

for i in range(2, n+1):
    print(answer[i])  # 정답 출력 