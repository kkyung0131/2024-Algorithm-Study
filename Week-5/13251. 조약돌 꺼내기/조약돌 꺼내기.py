D = [0] * 51  # 색깔별 조약돌 개수 저장 리스트 
prob = [0] * 51  # 색깔별 확률 저장 리스트 
m = int(input())  # 색의 종류 
D = list(map(int, input().split())) 
t = 0  # 전체 조약돌 개수 

# 조약돌 개수 더하기 
for i in range(0, m):
    t += D[i]

k = int(input())  # 선택 조약돌 개수
ans = 0  # 정답 변수 

for i in range(m):
    if D[i] >= k:  # 현재 색깔 조약돌 개수가 선택 개수보다 크면 
        prob[i] = 1  # 확률 1 저장 
        for j in range(k):
            prob[i] = prob[i] * (D[i]-j) / (t-j)  # 확률 계산 
        ans += prob[i]  # 정답에 더하기 

print(ans)