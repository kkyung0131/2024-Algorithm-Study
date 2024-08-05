
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 레슨 개수, 블루레이 개수
A = list(map(int, input().split()))  # 레슨 데이터 저장 리스트
s = 0  # 시작 인덱스 선언
e = 0  # 끝 인덱스 선언 

for i in A:
    if s < i:
        s = i  # 시작 인덱스는 최댓값
    e += i  # 끝 인덱스는 총합 

while s <= e:
    medi = int((s+e)/2)  # 중앙값 인덱스 
    sum = 0  # 합 
    count = 0  # 개수 
    for i in range(n):
        if sum + A[i] > medi:
            count += 1 
            sum = 0  # 초기화 
        sum += A[i]
    if sum != 0:
        count += 1 
    if count > m: 
        s = medi + 1 
    else:
        e = medi - 1 

print(s)