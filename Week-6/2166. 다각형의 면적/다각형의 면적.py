import sys
input = sys.stdin.readline
n = int(input())  # 점의 개수
x = []  # x좌표 저장 리스트
y = []  # y좌표 저장 리스트 

for i in range(n):
    tempX, tempY = map(int, input().split())
    x.append(tempX)
    y.append(tempY)

x.append(x[0])
y.append(y[0])

result = 0  # 넓이 저장 

for i in range(n):
    result += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

print(round(abs(result/2), 1))