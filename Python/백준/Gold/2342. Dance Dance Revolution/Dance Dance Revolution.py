import sys
input = sys.stdin.readline

# D[N][L][R] : N개 인풋, 왼쪽 다리 L, 오른쪽 다리 R에 있을 때 힘의 최솟값
D = [[[sys.maxsize for k in range(5)] for j in range(5)] for i in range(100001)]

# 한 발 이동 시 드는 힘을 미리 저장 
M = [[0, 2, 2, 2, 2],
     [2, 1, 3, 4, 3],
     [2, 3, 1, 3, 4],
     [2, 4, 3, 1, 3],
     [2, 3, 4, 3, 1]]
      
s = 1 
D[0][0][0] = 0  # 처음에는 아무 힘이 들지 않은 상태로 시작 

inputList = list(map(int, input().split()))
index = 0 

while inputList[index] != 0:
    n = inputList[index]
    for i in range(5):  
        if n == i:  # 두 발이 같은 자리에 있을 수 없음 
            continue 
        for j in range(5):  # 오른쪽 다리 이동 
            D[s][i][n] = min(D[s-1][i][j]+M[j][n], D[s][i][n]) 
    
    for j in range(5):  
        if n == j:
            continue
        for i in range(5):  # 왼쪽 다리 이동 
            D[s][n][j] = min(D[s-1][i][j]+M[i][n], D[s][n][j])
    
    s += 1 
    index += 1 

s -= 1 
result = sys.maxsize

for i in range(5):
    for j in range(5):
        result = min(result, D[s][i][j])  # 모두 수행한 후 최솟값 찾기 

print(result)