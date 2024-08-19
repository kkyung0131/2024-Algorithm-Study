import sys
input = sys.stdin.readline

n = int(input())  # 노드 개수
tree = {}  # 딕셔너리 형태로 트리 데이터 저장 

# 트리 데이터 저장 
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회 : 중간 > 왼쪽 > 오른쪽
def preOrder(now):
    if now == '.':  # 자식 노드이면 종료
        return 
    print(now, end='')  # 현재 노드 출력 
    preOrder(tree[now][0])  # 왼쪽 노드 탐색 
    preOrder(tree[now][1])  # 오른쪽 노드 탐색 

# 중위 순회 : 왼쪽 > 중간 > 오른쪽 
def inOrder(now):
    if now == '.':
        return 
    inOrder(tree[now][0])
    print(now, end='')
    inOrder(tree[now][1])

# 후위 순회 : 왼쪽 > 오른쪽 > 중간 
def postOrder(now):
    if now == '.':
        return 
    postOrder(tree[now][0])
    postOrder(tree[now][1])
    print(now, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')