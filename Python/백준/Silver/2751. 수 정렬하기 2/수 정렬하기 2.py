import sys
input = sys.stdin.readline
print = sys.stdout.write

# 병합 정렬 함수 
def mergeSort(s,e):
    if s >= e: return  # 집합이 하나의 수로 이루어진 경우
    med = (s+e)//2  # 중앙값
    mergeSort(s,med) 
    mergeSort(med+1,e)
    for i in range(s, e+1):
        temp[i] = A[i]   # 임시 리스트에 값 저장
    
    # 두 집합 병합 
    k = s
    index1 = s
    index2 = med+1 
    # 더 작은 값을 리스트에 저장, 해당 인덱스를 1 증가 
    while index1 <= med and index2 <= e:
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            k += 1 
            index2 += 1
        else:
            A[k] = temp[index1]
            k += 1 
            index1 += 1 
    
    # 남아있는 값 정리 
    while index1 <= med:
        A[k] = temp[index1]
        k += 1 
        index1 += 1 
    
    while index2 <= e:
        A[k] = temp[index2]
        k += 1 
        index2 += 1 

n = int(input())
A = [0] * int(n+1)
temp = [0] * int(n+1)

for i in range(1, n+1):
    A[i] = int(input())
    
mergeSort(1,n)

for i in range(1, n+1):
    print(str(A[i]) + '\n')