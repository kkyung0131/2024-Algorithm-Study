import sys
input = sys.stdin.readline

n = int(input())  # 도시의 수
m = int(input())  # 여행 계획에 속한 도시의 수 
dosi = [[0 for j in range(n+1)] for i in range(n+1)]  # 도시 연결 데이터 리스트

# find 연산 구현
def find(a):
    if a == parent[a]:  # 대표 노드이면
        return a  # 반환 
    else:  # 대표 노드가 아니면
        parent[a] = find(parent[a])  # 대표 노드를 찾은 후 
        return parent[a]  # 반환 
    
# union 연산 구현 
def union(a,b):
    a = find(a)  # a의 대표 노드 찾기 
    b = find(b)  # b의 대표 노드 찾기 
    if a != b:  # 두 대표 노드가 다르면 
        parent[b] = a  # 연결 

# 도시 연결 데이터 저장 
for i in range(1, n+1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0,0)

route = list(map(int, input().split()))  # 여행 도시 저장 리스트 
route.insert(0,0)
parent = [0] * (n+1)  # 대표 노드 저장 리스트 

for i in range(1, n+1):
    parent[i] = i  # 대표 노드를 자기 자신 인덱스 값으로 초기화

# 인접 행렬에서 도시가 연결되어 있으면 union 연산 수행
for i in range(1, n+1):
    for j in range(1, n+1):
        if dosi[i][j] == 1:
            union(i,j)
            
index = find(route[1])
isConnect = True  # 연결 여부 

for i in range(2, len(route)):
    if index != find(route[i]):  # 대표 노드가 동일하지 않은 노드가 있다면 
        isConnect = False  # 연결되지 않음  
        break 

if isConnect:
    print("YES")
else:
    print("NO")