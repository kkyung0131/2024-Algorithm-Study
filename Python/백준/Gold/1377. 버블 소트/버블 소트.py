import sys
input = sys.stdin.readline

n = int(input())  # 데이터 개수
A = []  # 데이터 리스트

for i in range(n):
    A.append((int(input()),i))  # (데이터, 인덱스) 순서로 저장

maximum = 0
sorted_A = sorted(A)  # A 리스트 정렬 

for i in range(n):
    # 정렬 전 index - 정렬 후 index 최댓값 저장
    if maximum < sorted_A[i][1] - i:  
        maximum = sorted_A[i][1] - i

print(maximum + 1)  