import sys
input = sys.stdin.readline

n = int(input())  # 숫자 개수
cnt = [0] * 10001  # 10,001 크기의 리스트 선언

# 입력값에 해당하는 위치의 값 1 증가
for i in range(n):
    cnt[int(input())] += 1

for i in range(10001):
    if cnt[i] != 0:  # 값이 0이 아니면
        for _ in range(cnt[i]):  # 해당 값만큼 
            print(i)  # 숫자 반복 출력 