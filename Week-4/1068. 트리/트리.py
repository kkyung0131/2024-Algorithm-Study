import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())  # 노드 개수
visited = [False] * n  # 방문 기록 리스트 
tree = [[] for _ in range(n)]  # 트리 인접 리스트 
answer = 0  # 정답 변수 
p = list(map(int, input().split()))  # 입력 데이터 저장 리스트 

for i in range(n):
    if p[i] != -1:  # 루트 노드가 아니면
        tree[i].append(p[i])
        tree[p[i]].append(i)  # 트리 데이터 저장 
    else:
        root = i  # 루트 노드값 저장 

# DFS 구현
def DFS(v):
    global answer
    visited[v] = True  # 방문 기록 
    c = 0 
    for i in tree[v]:
        if not visited[i] and i != deleteNode:
            c += 1 
            DFS(i)
    if c == 0:
        answer += 1  # 자식 노드 수가 0개 이면 리프 노드로 간주 

deleteNode = int(input())  # 삭제 노드 

if deleteNode == root:  # 삭제 노드 값이 루트와 같으면
    print(0)
else:
    DFS(root)
    print(answer)