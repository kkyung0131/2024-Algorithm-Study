import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 수의 개수, 최솟값 구하는 횟수
h = 0  # 트리 높이
length = n  # 리프 노드의 개수 

# 트리 높이 구하기 
while length != 0:
    length //= 2
    h += 1 

size = pow(2, h+1)  # 트리 사이즈 
leftNodeStartIndex = size // 2 - 1  # 시작 인덱스  
tree = [sys.maxsize] * (size + 1)  # 최댓값으로 트리 리스트 초기화

# 데이터 리프 노드에 저장 
for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수
def setTree(index):
    while index != 1:
        if tree[index//2] > tree[index]:  # 부모노드가 현재 노드보다 크면 
            tree[index//2] = tree[index]  # 값 저장 
        index -= 1 
        
setTree(size - 1)  # 트리 생성 

# 최솟값 계산 함수 
def getMin(s, e):
    Min = sys.maxsize 
    while s <= e:
        if s % 2 == 1:
            Min = min(Min, tree[s])
            s += 1 
        if e % 2 == 0:
            Min = min(Min, tree[e])
            e -= 1 
        s //= 2 
        e //= 2 
    return Min 

for _ in range(m):
    s, e = map(int, input().split())
    s += leftNodeStartIndex 
    e += leftNodeStartIndex
    print(getMin(s, e))