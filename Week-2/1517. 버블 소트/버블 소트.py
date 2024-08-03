import sys
input = sys.stdin.readline

result = 0  # 결과 

# 병합 정렬 함수
def mergeSort(s,e):
    global result
    
    if s >= e: return
    med = (s+e)//2
    mergeSort(s, med)
    mergeSort(med+1, e)
    
    for i in range(s, e+1):
        temp[i] = A[i]
    
    k = s
    index1 = s 
    index2 = med+1 
    while index1 <= med and index2 <= e:
        # 뒤쪽 값 선택 > 앞쪽 그룹 데이터 개수 = swap 횟수 
        if temp[index1] > temp[index2]:
            A[k] = temp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1 
        else:
            A[k] = temp[index1]
            k += 1 
            index1 += 1 
    
    # 남은 값 채우기   
    while index1 <= med:
        A[k] = temp[index1]
        k += 1 
        index1 += 1 
    while index2 <= e:
        A[k] = temp[index2]
        k += 1 
        index2 += 1 
        
n = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)  # A의 인덱스를 1부터 시작하기 위해 0번 인덱스에 0을 추가 
temp = [0] * int(n+1)

mergeSort(1,n)
print(result)