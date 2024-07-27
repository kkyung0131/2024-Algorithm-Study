import sys
input = sys.stdin.readline
n = int(input())  # 재료의 개수
m = int(input())  # 갑옷이 되는 번호 
A = list(map(int, input().split()))  # 재료 데이터 리스트로 저장
cnt = 0  # 개수
i = 0  # 왼쪽 인덱스
j = n-1  # 오른쪽 인덱스 

A.sort()  # A 리스트 정렬
while i < j:  # 두 포인터가 교차하기 전까지
    if A[i]+A[j] < m:  # 합이 m보다 작으면
        i += 1  # 왼쪽 인덱스 하나 증가
    elif A[i]+A[j] > m:  # 합이 m보다 크면
        j -= 1  # 오른쪽 인덱스 하나 감소
    else:  # 합이 m과 같으면
        cnt += 1  # 개수 1 증가
        i += 1  # 양쪽 인덱스 모두 이동 
        j -= 1 

print(cnt)