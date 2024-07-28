import sys

# input 함수보다 sys.stdin.readline이 더 빠르게 동작
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())  # 숫자 개수(N), 질의 개수(M)
numbers = list(map(int, input().split()))  # 숫자 데이터를 리스트로 저장
prefix_sum = [0]  # 합 배열 변수 선언
temp = 0  

# 합 배열 생성
for i in numbers:
    temp = temp + i  # 누적합 계산 후
    prefix_sum.append(temp)  # 합 배열에 추가
    
# 구간 합 계산
for i in range(quizNo):
    s, e = map(int, input().split())  # s번째 수부터 e번째 수까지 합 출력
    print(prefix_sum[e] - prefix_sum[s-1])  # 구간 합 출력 
