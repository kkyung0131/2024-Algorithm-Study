import sys
input = sys.stdin.readline

from collections import deque

# 상하좌우 탐색을 위한 리스트 선언
dx = [0,1,0,-1]
dy = [1,0,-1,0]

n, m = map(int, input().split())  # row, column
matrix = [[0]*m for _ in range(n)]  # 미로
visited = [[False]*m for _ in range(n)]  # 방문 기록 행렬 

for i in range(n):
    numbers = list(input())  # 입력을 한 자릿수씩 받아서 리스트로 저장
    for j in range(m):
        matrix[i][j] = int(numbers[j])  # 행렬에 값 저장 

# BFS 구현
def BFS(i,j):
    queue = deque()  # 큐 선언 
    queue.append((i,j))  # 시작점 삽입
    visited[i][j] = True  # 방문 기록 
    
    while queue:
        now = queue.popleft()  # 노드 데이터 가져오기
        for k in range(4):  # 상하좌우 탐색 
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x>=0 and y>=0 and x<n and y<m:  # 좌표가 유효하면
                if matrix[x][y] != 0 and not visited[x][y]:  # 이동 가능하고 미방문 노드이면 
                    visited[x][y] = True  # 방문 기록 
                    matrix[x][y] = matrix[now[0]][now[1]] + 1  # depth 업데이트
                    queue.append((x,y))  # 삽입 
    
BFS(0,0)
print(matrix[n-1][m-1])