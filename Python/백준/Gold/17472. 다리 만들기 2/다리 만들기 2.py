import sys
import copy
from collections import deque
from queue import PriorityQueue
input = sys.stdin.readline

# 네 방향 탐색을 위한 상수
dr = [0,1,0,-1]
dc = [1,0,-1,0]

n, m = map(int, input().split())  # 행렬 크기 
myMap = [[0 for j in range(m)] for i in range(n)]  # 맵 정보 저장 리스트
visited = [[False for j in range(m)] for i in range(n)]  # 방문 기록 리스트 

# 지도 정보 저장
for i in range(n):
    myMap[i] = list(map(int, input().split()))

num = 1  # 섬 번호 
alist = list([])  # 모든 섬 정보 리스트 
mlist = []  # 1개의 섬 정보 리스트 

# 섬에 노드를 더해주는 함수 구현
def addNode(i, j, queue):
    myMap[i][j] = num  # i, j 위치에 섬 번호 저장 
    visited[i][j] = True # 방문 기록 
    mlist.append([i,j])  # 섬 정보에 노드 추가
    queue.append([i,j])  # 큐에 노드 추가 

# BFS 구현 
def BFS(i,j):
    queue = deque()  # 큐 선언 
    mlist.clear()  # 리스트 초기화 
    start = [i,j]  
    queue.append(start)  # 시작 노드 큐에 삽입 
    mlist.append(start)  # 시작 노드 섬 정보에 추가 
    visited[i][j] = True  # 방문 기록 
    myMap[i][j] = num  # 섬 번호 저장 
    while queue:
        r, c = queue.popleft()  # 현재 위치치 pop 
        for d in range(4):  # 네 방향으로 탐색 
            tempR = dr[d]
            tempC = dc[d]
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                if not visited[r+tempR][c+tempC] and myMap[r+tempR][c+tempC] != 0:
                    addNode(r+tempR, c+tempC, queue)  
                else:
                    break
                if tempR < 0:
                    tempR -= 1 
                elif tempR > 0:
                    tempR += 1 
                elif tempC < 0:
                    tempC -= 1 
                elif tempC > 0:
                    tempC += 1
    return mlist 

# 섬 구분 작업 수행 
for i in range(n):
    for j in range(m):
        if myMap[i][j] != 0 and not visited[i][j]:
            tempList = copy.deepcopy(BFS(i,j))  # 섬 정보 가져오기, 깊은 복사로 진해해서 주소 공유 x 
            num += 1  # 섬 값 하나 증가 
            alist.append(tempList)  # 섬 정보 추가 

pq = PriorityQueue()  # 우선순위 큐 선언 

for now in alist:  # 인접 노드 
    for temp in now:
        r = temp[0]
        c = temp[1]
        now_S = myMap[r][c]  # 섬 정보 추출 
        for d in range(4):  # 4방향 검색 
            tempR = dr[d]
            tempC = dc[d]
            blength = 0 
            while r + tempR >= 0 and r + tempR < n and c + tempC >= 0 and c + tempC < m:
                if myMap[r+tempR][c+tempC] == now_S:  # 같은 섬이면 엣지 형성 불가 
                    break
                elif myMap[r+tempR][c+tempC] != 0:  # 같은 섬도, 바다도 아니면 
                    if blength > 1:  # 길이가 1 이상이면 
                        pq.put((blength, now_S, myMap[r+tempR][c+tempC]))  # 큐에 추가 
                    break
                else:  # 바다이면 
                    blength += 1  # 다리 길이 연장 
                if tempR < 0:
                    tempR -= 1
                elif tempR > 0:
                    tempR += 1 
                elif tempC < 0:
                    tempC -= 1 
                elif tempC > 0:
                    tempC += 1 

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a 

parent = [0] * num  # 대표 노드 저장 리스트 

# 대표 노드 리스트 초기화 
for i in range(len(parent)):
    parent[i] = i 
    
useEdge = 0  # 사용한 엣지의 수
result = 0  # 정답 변수 

while pq.qsize() > 0: 
    v, s, e = pq.get()  # 엣지 정보 가져오기 
    if find(s) != find(e):  # 부모 노드가 다르면 = 사이클이 생기지 않으면 
        union(s,e)  # 연결 
        result += v  # 정답 변수에 가중치 더하기 
        useEdge += 1  # 엣지의 수 1 증가 

if useEdge == num - 2:  # 섬의 번호 표시를 위해 -2 연산 
    print(result)
else:
    print(-1)