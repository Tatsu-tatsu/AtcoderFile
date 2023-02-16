from collections import defaultdict
NIL = -1

class Node():
    def __init__(self, parent=NIL, left=NIL, right=NIL):
      self.parent = parent
      self.left = left
      self.right = right

def pre_parse(u):
  if u == NIL:
    return
  print(u, end=" ")
  pre_parse(tree[u].left)
  pre_parse(tree[u].right)

def in_parse(u):
  if u == NIL:
    return
  in_parse(tree[u].left)
  print(u, end=" ")
  in_parse(tree[u].right)

def post_parse(u):
  if u == NIL:
    return
  post_parse(tree[u].left)
  post_parse(tree[u].right)
  print(u, end=" ")

n = int(input())
tree = defaultdict(Node)
for i in range(n):
  id, left, right = map(int, input().split())
  tree[id].left = left
  tree[id].right = right
  if left != NIL:
    tree[left].parent = id
  if right != NIL:
    tree[right].parent = id

root = 0

for i in range(n):
  if tree[id].parent == NIL:
    root = i

print("Preorder")
pre_parse(root)
print("Inorder")
in_parse(root)
print("Postorder")
post_parse(root)