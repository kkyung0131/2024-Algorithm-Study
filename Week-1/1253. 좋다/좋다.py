import sys
input = sys.stdin.readline

n = int(input())  # 데이터 개수
result = 0  # 좋은 수 개수
A = list(map(int, input().split()))  # 리스트 저장
A.sort()  # 리스트 정렬

for k in range(n):
    find = A[k]
    i = 0
    j = n-1 
    while i < j:
        if A[i] + A[j] == find:  # 일치하면 
            if i!=k and j!=k:  # 예외
                result += 1  # 좋은 수 개수 1 증가
                break  # while문 종료
            elif i == k:  # i가 k이면 
                i += 1 
            elif j == k:  # j가 k이면 
                j -= 1
        elif A[i] + A[j] < find:  # 합이 더 작으면
            i += 1  # 왼쪽 인덱스 1 증가 
        else:  # 합이 더 크면
            j -= 1  # 오른쪽 인덱스 1 증가 
print(result)
