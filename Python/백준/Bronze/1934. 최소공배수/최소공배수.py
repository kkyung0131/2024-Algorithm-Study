import sys
input = sys.stdin.readline

# 최대 공약수 함수
def gcd(a,b):
    if b == 0:  # b가 0이면
        return a  # a가 최대 공약수 
    else:
        return gcd(b,a%b)  # 재귀함수 형태로 구현

t = int(input())  # 테스트 케이스

for i in range(t):
    a, b = map(int, input().split())  
    result = a*b/gcd(a,b)  # 최소 공배수
    print(int(result))  # 결과 출력 