import sys
input = sys.stdin.readline

n = int(input())  # 수 개수
A = list(map(int, input().split()))  # 수 저장 리스트
m = int(input())  # 탐색할 수 개수 
target_list = list(map(int, input().split()))  # 탐색할 수 저장 리스트 

A.sort()  # 정렬 O(nlogn)


# m개의 수 탐색
for i in range(m):
    find = False  # 플래그
    target = target_list[i]  # 찾아야 하는 수 
    s = 0  # 시작 인덱스
    e = len(A)-1  # 끝 인덱스 
    while s <= e:
        medi = int((s+e)/2)  # 중앙값 인덱스 
        medv = A[medi]  # 중앙값 
        if medv > target:  # 중앙값이 타깃보다 크면 
            e = medi - 1  # 왼쪽에서 탐색 
        elif medv < target:  # 중앙값이 타깃보다 작으면 
            s = medi + 1  # 오른쪽에서 탐색 
        else:
            find = True  # 탐색 성공 
            break
    if find: print(1)  # 탐색 성공이면 1 출력
    else: print(0)  # 아니면 0 출력 