import sys
input = sys.stdin.readline

n = int(input())  # 수열 개수
A = list(map(int, input().split()))  # 수열 데이터 저장 리스트
A.insert(0,0)

index = 0
maxLength = 1
B = [0] * 1000001
D = [0] * 1000001
ans = [0] * 1000001
B[maxLength] = A[1]  # B[1] = A[1]으로 초기화
D[1] = 1 

# binary search 구현
def binarySearch(l, r, now):
    while l < r:
        mid = (l+r)//2  # 중앙값
        if B[mid] < now:
            l = mid + 1 
        else:
            r = mid 
    return l 

for i in range(2, n+1):
    if B[maxLength] < A[i]:  # 가장 마지막 수열보다 현재 수열이 크면 
        maxLength += 1 
        B[maxLength] = A[i]
        D[i] = maxLength 
    else:  
        index = binarySearch(1, maxLength, A[i])
        B[index] = A[i]
        D[i] = index 
        
print(maxLength)
index = maxLength 
x = B[maxLength] + 1 

# 뒤에서부터 탐색하면서 정답 수열 저장 
for i in range(n, 0, -1):
    if D[i] == index: 
        ans[index] = A[i]
        index -= 1 

for i in range(1, maxLength + 1):
    print(ans[i], end=' ')