import sys
input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]
    
# 전위 순회 (Root -> left -> right)
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])
        