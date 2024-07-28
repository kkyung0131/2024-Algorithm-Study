from queue import PriorityQueue  # 우선순위 큐
import sys
print = sys.stdout.write
input = sys.stdin.readline

n = int(input())  # 질의 요청 개수
myQueue = PriorityQueue()  # 우선순위 큐 선언

for i in range(n):
    x = int(input())
    if x == 0:
        if myQueue.empty():  # 큐가 비어있으면
            print('0\n')  # 0을 출력
        else:  # 큐가 비어있지 않으면
            print(str(myQueue.get()[1])+'\n')  # front 값 출력
    else:  # x != 0
        # 1) 절댓값을 기준으로 정렬 후 2) 음수 우선 정렬 
        myQueue.put((abs(x), x)) 