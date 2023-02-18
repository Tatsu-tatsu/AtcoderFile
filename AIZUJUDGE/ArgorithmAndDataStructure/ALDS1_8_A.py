from collections import defaultdict
class Node():
  def __init__(self):
      self.parent = None
      self.left = None
      self.right = None

def insert(root, key):
  if root == key:
    tree[key] = Node()
  else:
    tree[key] = Node()
    x = root
    while x != None:
      next_parent = x
      if key < x:
        x = tree[x].left
      else:
        x = tree[x].right
    tree[key].parent = next_parent
    if key < next_parent:
      tree[next_parent].left = key
    else:
      tree[next_parent].right = key

def in_order(u):
  if u == None:
    return
  in_order(tree[u].left)
  in_order_list.append(u)
  in_order(tree[u].right)

def pre_order(u):
  if u == None:
    return
  pre_order_list.append(u)
  pre_order(tree[u].left)
  pre_order(tree[u].right)

N = int(input())
tree = defaultdict(Node)
in_order_list = []
pre_order_list = []
for i in range(N):
  A = input().split()
  if A[0] == "insert":
    num = int(A[1])
    if i == 0:
      root = num
    insert(root, num)
  elif A[0] == "print":
    in_order(root)
    print(" ".join(map(str, in_order_list)))
    pre_order(root)
    print(" ".join(map(str, pre_order_list)))
    