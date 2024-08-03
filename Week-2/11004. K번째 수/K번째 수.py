import sys
input = sys.stdin.readline

n, k = map(int, input().split())  # 숫자의 개수, k번째 수
A = list(map(int, input().split()))  # 숫자 데이터 저장 배열


# 피벗 구하는 함수 
def getPivot(s, e):
    global A  # 전역변수 
    if (s + 1 == e):  
        if A[s] > A[e]:  
            swap(s,e) 
        return e 
    med = (s+e)//2  # 중앙값
    swap(s,med)  # 중앙값을 시작 위치와 swap
    pivot = A[s]  # pivot을 start 값으로 결정
    
    i = s+1  # 시작 인덱스
    j = e  # 끝 인덱스 
    
    while i <= j: 
        while pivot < A[j] and j > 0: 
            j -= 1
        while pivot > A[i] and i < len(A)-1:
            i += 1
        if i <= j:
            swap(i,j)
            i += 1; j -= 1 
    A[s] = A[j]
    A[j] = pivot
    return j 

# swap 함수 
def swap(i,j):
    global A
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

# 퀵 정렬 함수 - 재귀함수 
def quickSort(s, e, k):
    global A  # 전역변수
    if s < e:  # 만약 s가 e보다 작으면
        pivot = getPivot(s, e)  # 피벗 구하기
        if pivot == k:
            return
        elif pivot < k:  # k가 오른쪽에 존재, 오른쪽 그룹만 정렬 
            quickSort(pivot+1, e, k)
        else:  # k가 왼쪽에 존재, 왼쪽 그룹만 정렬 
            quickSort(s, pivot-1, k)
            
quickSort(0, n-1, k-1)  # 인덱스 0부터 시작하므로 1을 빼주어야 함 
print(A[k-1])