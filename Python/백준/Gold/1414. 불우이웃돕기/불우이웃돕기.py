import sys
from queue import PriorityQueue

input = sys.stdin.readline
n = int(input())  # 컴퓨터 개수
pq = PriorityQueue()  # 우선순위 큐 : 랜선 정보 저장 
mySum = 0  # 랜선의 합 저장 변수 

for i in range(n):
    c = list(input())  # 문자열 데이터
    for j in range(n):
        temp = 0
        if 'a' <= c[j] <= 'z':  # 소문자이면
            temp = ord(c[j]) - ord('a') + 1 
        elif 'A' <= c[j] <= 'Z':  # 대문자이면 
            temp = ord(c[j]) - ord('A') + 27
        mySum += temp  # 랜선 길이 더하기
        if i != j and temp != 0:  # 연결 랜선이 있다면 
            pq.put((temp, i, j))  # 큐에 랜선 정보 저장

parent = [0] * n  # 대표 노드 리스트 

for i in range(n):
    parent[i] = i  # 대표 노드 리스트 초기화 

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
result = 0  # 결괏값 저장 변수 

# MST 수행 
while pq.qsize() > 0:
    v, s, e = pq.get()
    if find(s) != find(e):
        union(s,e)
        result += v 
        useEdge += 1 

if useEdge == n-1:
    print(mySum - result)
else:
    print(-1)