import math
import sys
input = sys.stdin.readline

A, B = map(int, input().split())  # 시작 수, 종료 수
prime = [0] * (10000001)

# 소수 리스트 값을 인덱스 값으로 초기화 
for i in range(2, len(prime)):
    prime[i] = i

# 2~10^14의 제곱근까지만 수행 
for i in range(2, int(math.sqrt(len(prime))+1)):
    if prime[i] == 0:  # 소수가 아니면
        continue  # 패스
    for j in range(i+i, len(prime), i):
        prime[j] = 0  # 배수 지우기

cnt = 0  # 출력값
for i in range(2, 10000001):
    if prime[i] != 0:  # 소수이면 
        temp = prime[i]
        # 소수의 제곱수들이 A와 B 사이 값인지 판단 
        while prime[i] <= B/temp:
            if prime[i] >= A/temp:
                cnt += 1
            temp = temp*prime[i]
print(cnt)
