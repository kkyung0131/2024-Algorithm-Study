import sys
input = sys.stdin.readline

F = [0] * 21  # 자리별로 만들 수 있는 경우의 수 저장 리스트 
S = [0] * 21  # 순열 저장 리스트 
visited = [False] * 21  # 방문 기록(숫자 사용 여부) 리스트 
n = int(input())  # 순열 길이 

# 팩토리얼 초기화
F[0] = 1 
for i in range(1, n+1):
    F[i] = F[i-1] * i 

inputList = list(map(int, input().split()))  # 문제 종류와 순열 데이터 받기 

if inputList[0]==1:  # 순열 출력 문제 
    k = inputList[1]  # 몇 번째 순열을 입력할지 
    for i in range(1, n+1):
        cnt = 1
        for j in range(1, n+1):
            if visited[j]:  # 사용한 숫자면 패스 
                continue 
            if k <= cnt*F[n-i]:
                k -= (cnt-1) * F[n-i]
                S[i] = j 
                visited[j] = True
                break 
            cnt += 1 
    for i in range(1, n+1):
        print(S[i], end=' ')
else:  # 순열 순서 출력 문제 
    k = 1  # 순열 순서 저장 
    for i in range(1, n+1):
        cnt = 0
        for j in range(1, inputList[i]):
            if not visited[j]:  # 방문하지 않았으면 
                cnt += 1  # 카운트 
        k += cnt * F[n-i]
        visited[inputList[i]] = True
    print(k)