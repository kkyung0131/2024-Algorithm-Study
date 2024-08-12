import sys 
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())  
IsEven = True  # 이분 그래프 판별 변수

# DFS 구현
def DFS(v):
    global IsEven
    visited[v] = True  # 방문 기록 
    for i in A[v]:
        if not visited[i]:  # 미방문이면
            check[i] = (check[v]+1)%2  # 다른 집합으로 처리
            DFS(i)  # 재귀함수 
        elif check[v] == check[i]:  # 이미 방문한 노드가 현재 노드와 같은 집합이면 
            IsEven = False  # 이분 그래프 아님 

for _ in range(n):
    v, e = map(int, input().split())  # 노드 개수, 엣지 개수 
    A = [[] for _ in range(v+1)]
    visited = [False] * (v+1)
    check = [0] * (v+1)
    IsEven = True  # 이분 그래프 
    
    for i in range(e):
        start, end = map(int, input().split())
        A[start].append(end)
        A[end].append(start)  # 인접 리스트에 데이터 저장
    
    for i in range(1, v+1):
        if IsEven:
            DFS(i)  # 모든 노드에 대해 DFS 실행행
        else:
            break
    
    # 결과 출력 
    if IsEven:
        print("YES")
    else:
        print("NO")