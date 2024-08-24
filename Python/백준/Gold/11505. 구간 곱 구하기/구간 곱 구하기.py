import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())  # 수의 개수, 변경 횟수, 구간 곱 횟수 
h = 0  # 트리 높이
length = n  # 리프 노드 개수 
MOD = 1000000007

# 트리 높이 구하기
while length != 0:
    length //= 2
    h += 1 

size = pow(2, h+1)  # 트리 사이즈 
leftNodeStartIndex = size // 2 - 1  # 시작 인덱스 
tree = [1] * (size + 1)  # 1로 초기화한 트리 리스트 

# 데이터 리프 노드에 저장 
for i in range(leftNodeStartIndex+1, leftNodeStartIndex+n+1):
    tree[i] = int(input())

# 인덱스 트리 생성 함수 
def setTree(index):
    while index != 1:
        tree[index//2] = tree[index//2] * tree[index] % MOD
        index -= 1 

setTree(size-1)

# 값 변경 함수 
def changeVal(index, value):
    tree[index] = value 
    while index > 1:
        index //= 2
        tree[index] = tree[index*2] % MOD * tree[index*2+1] % MOD 

# 구간 곱 계산 함수 
def getMul(s,e):
    partMul = 1
    while s <= e:
        if s % 2 == 1:
            partMul = partMul * tree[s] % MOD
            s += 1 
        if e % 2 == 0:
            partMul = partMul * tree[e] % MOD 
            e -= 1 
        s //= 2 
        e //= 2 
    return partMul

for _ in range(m+k):
    question, s, e = map(int, input().split())
    if question == 1:
        changeVal(leftNodeStartIndex+s,e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getMul(s,e))