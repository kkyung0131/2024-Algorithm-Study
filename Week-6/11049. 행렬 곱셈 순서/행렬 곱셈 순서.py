import sys
input = sys.stdin.readline

n = int(input())  # 행렬 개수
m = []  # 행렬 저장 리스트
D = [[-1 for j in range(n+1)] for i in range(n+1)]  # DP 테이블 

m.append((0,0))

# m에 행렬 데이터 저장 
for i in range(n):
    x, y = map(int, input().split())
    m.append((x,y))

# 함수 정의 - top-down 방식
def execute(s,e):
    result = sys.maxsize 
    if D[s][e] != -1:  # 이미 계산된 부분이면
        return D[s][e]  # 다시 계산하지 않고 값 리턴 
    if s == e:  # 1개 행렬의 연산이면
        return 0  # 0을 리턴 
    if s+1 == e:  # 2개 행렬의 연산이면 
        return m[s][0] * m[s][1] * m[e][1]  # 연산 횟수 계산하여 출력 
    for i in range(s,e):  # 3개 행렬의 연산이면 재귀 형태로 계산 
        result = min(result, execute(s,i)+execute(i+1,e)+(m[s][0]*m[i][1]*m[e][1]))
    D[s][e] = result
    return D[s][e]

print(execute(1,n))