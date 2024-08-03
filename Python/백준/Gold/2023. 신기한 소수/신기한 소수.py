import sys
sys.setrecursionlimit(10*4)  # 최대 재귀 깊이 설정
input = sys.stdin.readline

n = int(input())  # 자릿수

# 소수 구하기 함수
def isPrime(num):
    for i in range(2, int(num/2+1)):
        if num % i == 0:  # 나눠지면
            return False  # 소수가 아님
    return True

# DFS 구현 
def DFS(num):
    if len(str(num)) == n:  # 최대 자릿수에 도달하면
        print(num)  # num 출력
    else:
        for i in range(1,10):
            # 홀수이고 소수이면
            if (i%2!=0) and (isPrime(num*10+i)):
                DFS(num*10+i)  # 자릿수 늘림

DFS(2)
DFS(3)
DFS(5)
DFS(7)