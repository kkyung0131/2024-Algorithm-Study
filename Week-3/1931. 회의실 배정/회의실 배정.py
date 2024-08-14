import sys
input = sys.stdin.readline

n = int(input())  # 회의 개수
A = [[0]*2 for _ in range(n)]  # 회의 시간 정보 저장

for i in range(n):
    s, e = map(int, input().split())  # 시작시각, 종료시각
    A[i][0] = e  # 종료시각 우선 정렬을 위해 먼저 저장 
    A[i][1] = s  # 시작시각 나중에 저장 

A.sort()  # 정렬 
cnt = 0  # 총 회의 수를 저장할 변수 
end = -1  # 종료시각 

for i in range(n):
    if A[i][1] >= end:  # 겹치지 않는 다음 회의가 나온 경우 
        end = A[i][0]  # 종료시각 업데이트
        cnt += 1  # 회의 수 1 증가 

print(cnt)