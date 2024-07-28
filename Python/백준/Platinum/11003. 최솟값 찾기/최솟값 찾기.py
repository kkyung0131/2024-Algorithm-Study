from collections import deque  # 덱 자료구조
n, l = map(int, input().split())  # 데이터 개수, 최솟값 구하는 범위
mydeque = deque()  # 덱 자료구조 선언
now = list(map(int, input().split())) 

for i in range(n):
    # mydeque에 값이 존재하고, 현재 수보다 큰 값을 가지면
    while (mydeque) and (mydeque[-1][0] > now[i]):
        mydeque.pop()  # 제거
    mydeque.append((now[i],i))  # 현재 수와 인덱스 값 추가
    if mydeque[0][1] <= i - l:  # 범위에서 벗어나면
        mydeque.popleft()  # 왼쪽값 제거 
    print(mydeque[0][0], end=' ')