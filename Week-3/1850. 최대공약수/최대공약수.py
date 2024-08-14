import sys
input = sys.stdin.readline

# 최대 공약수 함수
def gcd(a,b):
    if b==0:  # b가 0이면
        return a  # a가 최대 공약수
    else:
        return gcd(b, a%b)  # 재귀함수로 구현
        
a, b = map(int, input().split())
result = gcd(a,b)  # 최대공약수 

while result > 0:
    print(1, end='')  # result만큼 1을 반복해서 출력 
    result -= 1 