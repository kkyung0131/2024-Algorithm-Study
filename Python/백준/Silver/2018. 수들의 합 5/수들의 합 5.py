n = int(input())  # 자연수 입력 받기

# 변수 초기화
cnt = 1  # 경우의 수 
start_idx = 1  # 시작 포인터
end_idx = 1   # 종료 포인터
sum = 1  # 누적합

while end_idx != n:
    if sum == n:  # 누적합이 입력한 자연수와 같으면
        cnt += 1  # 경우의 수 증가
        end_idx += 1  # 종료 인덱스 증가
        sum += end_idx  # sum 값 변경
    
    elif sum > n:  # 누적합이 입력한 자연수보다 크면
        sum -= start_idx  # sum 값 변경 
        start_idx += 1  # 시작 인덱스 증가 
    
    else:  # 누적합이 입력한 자연수보다 작으면
        end_idx += 1  # 종료 인덱스 증가 
        sum += end_idx  # sum 값 변경 

print(cnt)  # 경우의 수 출력 