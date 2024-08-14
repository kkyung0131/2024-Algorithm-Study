import sys
input = sys.stdin.readline

n = int(input())
A = [[] for _ in range(n)]  # 인접 리스트
visited = [False] * (n)  # 방문 기록 리스트 
D = [0] * (n)  # 각 노드 값 저장 리스트 
lcm = 1  # 최소 공배수 

# 최대 공약수 함수 구현
def gcd(a,b):
    if b==0:
        return a 
    else:
        return gcd(b,a%b)

# 탐색 함수 구현 
def DFS(v):
    visited[v] = True
    for i in A[v]:
        next = i[0]
        if not visited[next]:
            D[next] = D[v] * i[2] // i[1]  # 다음 노드의 값 저장 
            DFS(next)

for i in range(n-1):
    a, b, p, q = map(int, input().split())
    A[a].append((b,p,q))
    A[b].append((a,q,p))  # 인접리스트 저장 
    lcm *= (p*q // gcd(p,q))  # 최소 공배수 계산 
    
D[0] = lcm  # 0번 노드에 최소 공배수 저장 
DFS(0)  # 0번 노드에서 DFS 수행 
mgcd = D[0]

for i in range(1,n):
    mgcd = gcd(mgcd, D[i])  # 업데이트된 리스트의 최대공약수 계산 

for i in range(n):
    print(int(D[i]//mgcd), end=' ') 