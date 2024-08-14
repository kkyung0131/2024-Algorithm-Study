import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 사람 수, 파티 개수
trueP = list(map(int, input().split()))  # 진실을 아는 사람 
T = trueP[0]  # 진실을 아는 사람 수 
del trueP[0]

result = 0  # 결과값 
party = [[] for _ in range(m)]  # 파티 데이터

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

# 두 원소가 같은 집합인지 확인하는 연산 
def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True 
    return False 

# 파티 데이터 저장
for i in range(m):
    party[i] = list(map(int, input().split()))
    del party[i][0]

parent = [0] * (n+1)  # 대표 노드 저장 리스트 
for i in range(n+1):
    parent[i] = i

# 파티에 참여한 사람을 1개의 그룹으로 생성 
for i in range(m):
    firstPeople = party[i][0] 
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

# 각 파티의 대표 노드와 진실을 아는 사람들의 대표 노드가 같다면 과장할 수 없음
for i in range(m):
    isPossible = True 
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        if find(firstPeople) == find(trueP[j]):  # 모두 같으면 
            isPossible = False
            break 
        
    if isPossible:  # 과장 가능하면 = 모두 다르면 
        result += 1  # 결과 1 증가 

print(result)