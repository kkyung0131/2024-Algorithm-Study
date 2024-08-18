import sys
from collections import deque
input = sys.stdin.readline

n = int(input())  # 건물 수
A = [[] for _ in range(n+1)]  # 건물 데이터 저장 인접 리스트
indegree = [0] * (n+1)  # 진입 차수 리스트 초기화 
selfBuild = [0] * (n+1)  # 자기 자신을 찾는 데 걸리는 시간 리스트 초기화 
result = [0] * (n+1)  # 결과 리스트 

for i in range(1, n+1):  # 건물 개수만큼 반복 
    inputList = list(map(int, input().split()))
    selfBuild[i] = (inputList[0])  # 건물을 짓는 데 걸리는 시간 
    index = 1 
    while True:
        preTemp = inputList[index]
        index += 1 
        if preTemp == -1:
            break
        A[preTemp].append(i)  # 인접 리스트 데이터 저장 
        indegree[i] += 1  # 진입 차수 데이터 저장 
    
queue = deque()  # 큐 선언

for i in range(1, n+1):
    if indegree[i] == 0:  # 진입 차수 값이 0이면
        queue.append(i)  # 큐에 삽입

while queue:
    now = queue.popleft()  # 현재 노드 pop
    for next in A[now]:  # 인접 노드에 대해서 
        indegree[next] -= 1  # 진입 차수 1 감소 
        result[next] = max(result[next], result[now] + selfBuild[now])  # 결과 노드를 업데이트
        if indegree[next] == 0:  # 진입 차수가 0 이면 
            queue.append(next)  # 큐에 삽입 

for i in range(1, n+1):
    print(result[i] + selfBuild[i])  # 결과 출력 