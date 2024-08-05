import sys
input = sys.stdin.readline

from queue import PriorityQueue
n = int(input())  # 카드 묶음 개수
queue = PriorityQueue()  # 우선순위 큐

# 큐에 데이터 저장
for _ in range(n):
    card = int(input())
    queue.put(card)

data1 = 0 
data2 = 0
result = 0

while queue.qsize() > 1:  
    data1 = queue.get()
    data2 = queue.get()  # 2개 카드 뽑기 
    temp = data1 + data2
    result += temp  # 2개 카드 더하기
    queue.put(temp)  # 다시 우선순위큐에 삽입 
    
print(result)