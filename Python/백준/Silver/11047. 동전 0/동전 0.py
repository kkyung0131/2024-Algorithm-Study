import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 동전 개수, 목표 금액
A = [0]*n  # 동전 리스트 선언 

# 동전 리스트 채우기
for i in range(n):
    A[i] = int(input())

cnt = 0  # 구성
for i in range(n-1, -1, -1):  # 역순으로 반복
    if A[i] <= k:  # 현재 동전의 가치가 k보다 작거나 같으면
        cnt += int(k/A[i])  # 구성에 추가 
        k = k % A[i]  # k를 남은 금액으로 갱신 

print(cnt)