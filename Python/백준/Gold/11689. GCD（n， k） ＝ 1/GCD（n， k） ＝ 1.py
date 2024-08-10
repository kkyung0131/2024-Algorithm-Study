import sys
input = sys.stdin.readline

import math
n = int(input())  # 소인수 표현
result = n  # 결과 

# 2~제곱근까지만 탐색
for i in range(2, int(math.sqrt(n))+1): 
    if n % i == 0:  # 소인수이면
        result -= result / i  # 결과 갱신 
        while n % i == 0:
            n /= i 

if n > 1:
    result -= result / n

print(int(result))