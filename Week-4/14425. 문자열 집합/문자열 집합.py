import sys
input = sys.stdin.readline

# Node 클래스 생성
class Node(object):
    def __init__(self, isEnd): 
        self.isEnd = isEnd  # 마지막 문자열 여부
        self.childNode = {}  # 자식 노드 

# Trie 클래스 생성 
class Trie(object):
    def __init__(self):
        self.parent = Node(None)   # 부모 노드 저장 변수 
    
    # 문자 삽입 함수
    def insert(self, string):
        now = self.parent
        length = 0 
        for char in string:  
            if char not in now.childNode:  # 자식 노드에 없는 문자면
                now.childNode[char] = Node(char)  # 새롭게 생성 
            now = now.childNode[char]  # 자식 노드로 이동 
            length += 1  
            if length == len(string):  # 마지막 문자이면 
                now.isEnd = True  # 마지막 문자임을 표시 
    
    # 문자 탐색 함수 
    def search(self, string):
        now = self.parent
        length = 0
        for char in string:
            if char in now.childNode:
                now = now.childNode[char]
                length += 1 
                if length == len(string) and now.isEnd==True:
                    return True 
            else:
                return False
        return False  # 문자 존재하지 않으면 False 리턴 

n, m = map(int, input().split())  # 문자열 개수, 검사할 문자열 개수 
myTrie = Trie()  # Trie 생성 

for _ in range(n):
    word = input().strip()
    myTrie.insert(word)  # 단어 삽입 
    
result = 0 
for _ in range(m):
    word = input().strip()
    if myTrie.search(word):  # 단어 탐색 
        result += 1 

print(result)