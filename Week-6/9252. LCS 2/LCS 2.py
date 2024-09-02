import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

A = list(input())  # 1번째 문자열
A.pop()  # \n 문자열 제거 
B = list(input())  # 2번째 문자열 
B.pop()  # \n 문자열 제거 

DP = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
path = []  # LCS 저장 리스트 

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:  # 값이 같으면
            DP[i][j] = DP[i-1][j-1] + 1  # 왼쪽 대각선 값 + 1로 저장 
        else:  # 다르면 
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])  # 왼족과 위의 값 중 큰 수 저장 

print(DP[len(A)][len(B)])  # LCS 길이 출력 

# LCS 재귀 형태로 구현 
def getText(r, c): 
    if r == 0 or c == 0:
        return
    if A[r-1] == B[c-1]:  # 같으면 
        path.append(A[r-1])  # LCS에 기록하고
        getText(r-1, c-1)  # 왼쪽 위로 이동 
    else:  # 다르면 
        if DP[r-1][c] > DP[r][c-1]:  # 왼쪽과 위 중 큰 수로 이동 
            getText(r-1, c)
        else:
            getText(r, c-1)

getText(len(A), len(B))

# 문자열 출력 
for i in range(len(path)-1, -1, -1):
    print(path.pop(i), end='')
print()