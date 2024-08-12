import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n, m = map(int, input().split())  # 원소 개수, 질의 개수 
parent = [0] * (n+1)  # 대표 노드 저장 리스트 

# find 연산 구현
def find(a):
    if a == parent[a]:  # 대표 노드이면 
        return a  # 반환
    else:  # 대표 노드가 아니면 대표 노드값 변경 
        parent[a] = find(parent[a])  # 재귀 형태로 구현하여 경로 압축
        return parent[a]
    
# union 연산 구현 
def union(a,b):
    a = find(a)
    b = find(b)  # find 연산 후 
    if a != b:  # 대표 노드가 다르면 
        parent[b] = a  # 하나의 집합으로 연결 

# 두 원소가 같은 집합인지 확인하는 함수 구현 
def checkSame(a,b):
    a = find(a)
    b = find(b)  # find 연산 후 
    if a == b:  # 값이 같으면 
        return True 
    else:
        return False 

for i in range(n+1):
    parent[i] = i  # 자기 인덱스 값으로 초기화 
    
for i in range(m):
    question, a, b = map(int, input().split())  # 질의, 첫번째 수, 두번째 수 
    if question == 0:  # 질의가 0이면 union 연산 
        union(a,b)
    else:  # 질의가 1이면 
        if checkSame(a,b):  # 같은 집합 원소인지 판단 
            print("YES")
        else:
            print("NO")