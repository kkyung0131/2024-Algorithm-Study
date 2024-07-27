checkList = [0]*4  # 'A', 'C', 'G', 'T' 확인
myList = [0]*4  
check = 0

# 새로 들어온 문자를 처리하는 함수
def myadd(c):
    global checkList, myList, check  # 전역변수
    if c == 'A':
        myList[0] += 1  # 현재 상태 리스트에서 A 1 증가
        if myList[0] == checkList[0]:  # 현재 상태와 체크 리스트가 같다면
            check += 1  # 충족한 문자의 수 1 증가
    elif c == 'C':
        myList[1] += 1  # 현재 상태 리스트에서 C 1 증가 
        if myList[1] == checkList[1]:
            check += 1 
    elif c == 'G':
        myList[2] += 1 
        if myList[2] == checkList[2]:
            check += 1 
    elif c == 'T':
        myList[3] += 1 
        if myList[3] == checkList[3]:
            check += 1

# 제거되는 문자를 처리하는 함수 
def myremove(c):
    global checkList, myList, check 
    if c == 'A':
        if myList[0] == checkList[0]:
            check -= 1 
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            check -= 1 
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            check -= 1 
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            check -= 1 
        myList[3] -= 1

S, P = map(int, input().split())  # 문자열 크기와 부분 문자열 크기 
result = 0  # 비밀번호 개수
A = list(input())  # 문자열 데이터
checkList = list(map(int, input().split()))  # 비밀번호 체크 리스트 

# 체크 리스트 값이 0인 개수만큼 check값 업데이트
for i in range(4):
    if checkList[i] == 0:
        check += 1

# 처음 윈도우
for i in range(P):
    myadd(A[i])
        
# 유효한 비밀번호 개수 계산
if check == 4:
    result += 1 

# 윈도우 이동하면서 제거되는 문자열과 새로 들어오는 문자열 처리 
for i in range(P, S):
    j = i - P 
    myadd(A[i])
    myremove(A[j])
    if check == 4:
        result += 1 

print(result)