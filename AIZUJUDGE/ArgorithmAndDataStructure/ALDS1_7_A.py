# 本通りだと、pythonは解けない。
# 深さは再帰関数で探す。
import sys
sys.setrecursionlimit(200000)
from collections import defaultdict
NIL = -1

class Node():
  def __init__(self, parent=NIL, left=NIL, right=NIL, children=[], depth=-1):
    self.parent = parent
    self.left = left # child
    self.right = right # sibling
    self.children = children
    self.depth = depth

def setDepth(u, d):
  if tree[u].depth != -1:
    return
  tree[u].depth = d
  for child in tree[u].children:
    setDepth(child, d+1)

n = int(input())
tree = defaultdict(Node)
root = 0
for i in range(n):
  C = list(map(int, input().split()))
  id = C[0]
  k = C[1]
  for j in range(k):
    tree[C[j+2]].parent = id
    if j == 0:
      tree[id].left = C[j+2]
    else:
      tree[C[j+1]].right = C[j+2] 
for u, node in tree.items():
  if node.parent == NIL:
    root = u
  ch = node.left
  children = []
  while ch != NIL:
    children.append(ch)
    ch = tree[ch].right
  node.children = children
setDepth(root, 0)

for u in sorted(set(tree)):
  node = tree[u]
  if node.parent == NIL:
    kind = "root" 
  else:
    if node.left == NIL:
      kind = "leaf"  
    else:
      kind = "internal node"
  # kind = "root" if node.parent == NIL else "leaf" if node.left == NIL else "internal node"(省略した版)
  print(f'node {u}: parent = {node.parent}, depth = {node.depth}, {kind}, {node.children}')
