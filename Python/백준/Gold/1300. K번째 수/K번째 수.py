import sys
input = sys.stdin.readline

n = int(input())  # 리스트 크기
k = int(input())  # 구하고자 하는 인덱스 

s = 1  # 시작 인덱스 
e = k  # 종료 인덱스 
ans = 0  # 정답 변수 선언

# 이진 탐색
while s <= e:
    medi = int((s+e)/2)
    cnt = 0 
    for i in range(1, n+1):
        cnt += min(int(medi/i), n)  # 작은 수를 카운트에 더함 
    if cnt < k:
        s = medi + 1 
    else:
        ans = medi
        e = medi - 1 

print(ans)