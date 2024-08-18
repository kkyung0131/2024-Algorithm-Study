import sys
from queue import PriorityQueue

input = sys.stdin.readline
n, m = map(int, input().split())  # 노드, 엣지 개수
pq = PriorityQueue()  # 우선순위 큐에 엣지 정보 저장
parent = [0] * (n+1)  # 대표 노드 저장 리스트 

# 대표 노드 값을 인덱스로 초기화
for i in range(n+1):
    parent[i] = i 

# 우선순위 큐에 엣지 정보 저장 
for i in range(m):
    s, e, w = map(int, input().split())
    pq.put((w,s,e))  # 자동 정렬 

# find 연산
def find(a):
    if a == parent[a]:
        return a 
    else:
        parent[a] = find(parent[a])
        return parent[a]

# union 연산
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a 

useEdge = 0  # 사용 엣지 수 저장 변수 
result = 0  # 정답 변수 

# MST 실행
while useEdge < n-1:  # 엣지 수가 N-1이 될 때까지 
    w, s, e = pq.get()  # 큐에서 엣지 정보를 가져옴 
    if find(s) != find(e):  # 같은 부모가 아니면 → 사이클이 생기지 않으면 
        union(s,e)  # union 연산 수행하고 
        result += w  # 가중치를 결과에 더하기 
        useEdge += 1  # 사용 엣지 수 업데이트 

print(result)