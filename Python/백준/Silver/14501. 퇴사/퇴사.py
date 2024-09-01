import sys
input = sys.stdin.readline

n = int(input())  # 남은 일 수
D = [0] * (n+2)  # 오늘부터 퇴사일까지 벌 수 있는 최대 수입
T = [0] * (n+1)  # 상담에 필요한 일 수
P = [0] * (n+1)  # 상담을 완료했을 때 받는 수입 

# T, P 리스트 입력 
for i in range(1, n+1):
    T[i], P[i] = map(int, input().split())

for i in range(n, 0, -1):
    if i+T[i] > n+1:  # i번째 상담을 퇴사일까지 끝낼 수 없을 때
        D[i] = D[i+1]
    else:   # i번째 상담을 퇴사일까지 끝낼 수 있을 때 
        D[i] = max(D[i+1], D[i+T[i]]+P[i]) 

print(D[1])