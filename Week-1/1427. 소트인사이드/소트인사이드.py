import sys
print = sys.stdout.write

A = list(input())  # 각 자릿수별로 나누어 리스트로 저장

# A 리스트 길이만큼 반복
for i in range(len(A)):
    maximum = i  # 현재 인덱스를 최댓값으로 설정(내림차순)
    # 남은 정렬 부분
    for j in range(i+1, len(A)):
        if A[j] > A[maximum]:
            maximum = j  # 최댓값 변경
    if A[i] < A[maximum]:  # swap
        temp = A[i]
        A[i] = A[maximum]
        A[maximum] = temp

for i in range(len(A)):
    print(A[i])
