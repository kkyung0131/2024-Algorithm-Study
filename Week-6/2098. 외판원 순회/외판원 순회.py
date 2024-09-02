import sys
input = sys.stdin.readline

n = int(input())  # 도시 개수
D = [[0 for j in range(1<<16)] for i in range(16)]  # DP 테이블
w = []  # i에서 j로 가는 데 드는 비용 저장 리스트 

# 반복문으로 w 리스트에 값 저장 
for i in range(n):
    w.append([])
    w[i] = list(map(int, input().split()))

# 완전 탐색 및 재귀 구현
def tsp(c, v):
    # 모든 노드를 방문한 경우 = v가 15=1111(2)인 경우
    if v == (1<<n)-1:
        if w[c][0] == 0:  # 시작 노드로 돌아갈 수 없으면
            return float('inf')  # 무한대 리턴 
        else:
            return w[c][0]
    
    # 이미 방문한 노드인 경우 값 리턴 
    if D[c][v] != 0:
        return D[c][v]

    min_val = float('inf')
    for i in range(0, n):
        # 방문한 적이 없고 갈 수 있는 도시인 경우 
        if (v & (1<<i)) == 0 and w[c][i] != 0:
            min_val = min(min_val, tsp(i,(v|(1<<i)))+w[c][i])
    D[c][v] = min_val
    return D[c][v]

print(tsp(0,1))