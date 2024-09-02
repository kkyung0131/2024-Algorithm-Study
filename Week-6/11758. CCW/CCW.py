import sys
input = sys.stdin.readline

# 세 점의 x, y 좌표값 저장
x1, y1 = map(int, input().split())  
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# CCW 공식
result = (x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3)

if result > 0:    # 반시계 방향 
    print(1)
elif result < 0:  # 시계 방향 
    print(-1) 
else:             # 일직선 
    print(0)