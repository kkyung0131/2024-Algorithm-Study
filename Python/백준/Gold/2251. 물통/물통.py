import sys
from collections import deque
input = sys.stdin.readline

# 0,1,2 = A,B,C
# A→B, A→C, B→A, B→C, C→A, C→B
sender = [0,0,1,1,2,2]
receiver = [1,2,0,2,0,1]

now = list(map(int, input().split()))  # A, B, C의 값 저장 
visited = [[False for j in range(201)] for i in range(201)]  # 방문 기록 리스트 
answer = [False] * 201

# BFS 구현
def BFS():
    queue = deque()  # 큐 자료구조 선언
    queue.append((0,0))  # 출발 노드 삽입 
    visited[0][0] = True  # 방문 기록 
    answer[now[2]] = True  # 정답 리스트에 체크
    while queue:
        now_Node = queue.popleft()  # 현재 노드 pop 
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B 
        for k in range(6):  # 6가지 케이스에 대해
            next = [A, B, C]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0 
            if next[receiver[k]] > now[receiver[k]]:  # 물이 넘치면
                # 넘치는 만큼 보내는 물통에 다시 넣어주기
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]  # 대상 물통 최대로 채우기 
            if not visited[next[0]][next[1]]:  # 미방문이면
                visited[next[0]][next[1]] = True  # 방문 기록 
                queue.append((next[0], next[1]))  # 삽입
                if next[0] == 0:  # A 물통이 비어있으면
                    answer[next[2]] = True  # C의 무게를 정답 변수에 저장

BFS()  # 탐색

for i in range(len(answer)):
    if answer[i]:
        print(i, end=' ')  # 출력 