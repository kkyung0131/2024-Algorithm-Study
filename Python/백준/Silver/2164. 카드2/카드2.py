from collections import deque
import sys
input = sys.stdin.readline

n = int(input())  # 카드 개수
myQueue = deque()  # 카드 저장 큐

# 큐에 카드를 순서대로 저장 
for i in range(1, n+1):
    myQueue.append(i)

while len(myQueue) > 1:  # 카드가 한 장 남을 때까지
    myQueue.popleft()  # 맨 위 카드 버리고
    myQueue.append(myQueue.popleft())  # 맨 위 카드 맨 아래로 이동 

print(myQueue[0]) 