import sys
import math
input = sys.stdin.readline

n = int(input())
prime = [0]*(10000001)

# 리스트 값을 인덱스 값으로 초기화 
for i in range(2, len(prime)):
    prime[i] = i
    
# 2~제곱근까지 탐색 수행
for i in range(2, int(math.sqrt(len(prime))+1)):
    if prime[i]==0:  # 소수가 아니면
        continue  # 패스
    for j in range(i+i, len(prime), i):
        prime[j] = 0  # 배수 지우기

# 팰린드롬 수 판별 함수
def isPalindrome(target):
    temp = list(str(target))  # 숫자를 리스트로 변환 
    s = 0  # 시작 인덱스 
    e = len(temp)-1  # 종료 인덱스 
    while s < e:
        if temp[s] != temp[e]:  # 값이 서로 다르면 
            return False 
        s += 1
        e -= 1  # 인덱스 한 칸 이동 
    return True  # 반복문 다 돌면 True 출력 

i = n 
while True:
    if prime[i] != 0:  # 소수이면
        result = prime[i]  
        if (isPalindrome(result)):  # 팰린드롬 수인지 판별 
            print(result)
            break 
    i += 1