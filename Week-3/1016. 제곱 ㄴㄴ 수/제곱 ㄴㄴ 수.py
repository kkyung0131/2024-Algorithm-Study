import sys
import math
input = sys.stdin.readline 

Min, Max = map(int, input().split())  # 최솟값, 최댓값
check = [False] * (Max-Min+1)  # 제곱수 판별 리스트 

for i in range(2, int(math.sqrt(Max)+1)):
    pow = i*i  # 제곱수 
    start_index = int(Min/pow)
    if Min % pow != 0:
        start_index += 1  # 나머지가 있으면 1을 더하고 시작
    for j in range(start_index, int(Max/pow)+1):  # 제곱수를 True로 변경
        check[int((j*pow)-Min)] = True 

cnt = 0
for i in range(0, Max-Min+1):
    if not check[i]:
        cnt += 1 
print(cnt)