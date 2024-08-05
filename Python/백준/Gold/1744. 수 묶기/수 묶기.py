import sys
input = sys.stdin.readline

from queue import PriorityQueue
n = int(input())
plus_pq = PriorityQueue()  # 양수 우선순위 큐
minus_pq = PriorityQueue()  # 음수 우선순위 큐 
one = 0
zero = 0

# 4개의 그룹으로 분리 저장
# 양수는 내림차순 정렬을 위해 -1을 곱해 저장
for i in range(n):
    data = int(input())
    if data > 1:
        plus_pq.put(data*-1)
    elif data==1:
        one += 1 
    elif data==0:
        zero += 1 
    else:
        minus_pq.put(data)

result = 0

# 양수 우선순위 큐
while plus_pq.qsize() > 1:
    first = plus_pq.get() * -1 
    second = plus_pq.get() * -1  # 두 개의 수를 뽑아서
    result += first * second   # 곱하고 결과에 더함 

if plus_pq.qsize() > 0:  # 수가 남아있다면
    result += plus_pq.get() * -1  # 더해주기 

# 음수 우선순위 큐
while minus_pq.qsize() > 1:
    first = minus_pq.get()  
    second = minus_pq.get()  # 두 개의 수를 뽑아서
    result += first * second   # 곱하고 결과에 더함 
    
if minus_pq.qsize() > 0:  # 수가 남아있고
    if zero == 0:  # 데이터 0이 하나도 없다면 
        result += minus_pq.get() 

result += one  # 1 처리 
print(result)