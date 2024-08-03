import sys
input = sys.stdin.readline

n = int(input())  # 사람 수
A = list(map(int, input().split()))  # 자릿수별로 구분해 리스트 저장
S = [0] * n  # 합 배열 리스트 초기화

# 삽입정렬 구현
"""for i in range(1,n):
    insert_point = i  # 삽입 위치
    insert_value = A[i]  # 삽입할 값
    for j in range(i-1, -1, -1):  # 삽입 가능 영역의 뒤에서부터 탐색
        if A[j] < A[i]:  # 값이 작은 것을 발견하면
            insert_point = j+1  # 삽입 위치 결정 
            break
        if j == 0:
            insert_point = 0  # 맨 앞에 삽입 
    for j in range(i, insert_point, -1):  # 데이터 하나씩 뒤로 밀기
        A[j] = A[j-1]
    A[insert_point] = insert_value  # 삽입"""


A.sort()  # 내장함수를 이용하면 시간복잡도 O(nlogn) 

    
# 합 배열 만들기
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

result = sum(S)

print(result)