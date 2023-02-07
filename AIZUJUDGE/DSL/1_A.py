class UnionFind():
  def __init__(self,n):
    self.n = n
    self.parents = [-1] * n
    self.rank = [1] * n

  def find(self, x):
    if self.parents[x] == -1:
      return x
    else:
      # パス圧縮：すべて同じ親に変更（必須）
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  
  def unite(self, x, y):
    a = self.find(x)
    b = self.find(y)
    if a == b:
      return
    # マージテク：rankを使って、木を長くなりすぎないようにする。実装は不必要。
    if self.rank[x] > self.rank[y]:
      self.parents[y] = x
    elif self.rank[x] < self.rank[y]:
      self.parents[x] = y 
    elif self.rank[x] == self.rank[y]:
      self.rank[x] += 1
      self.parents[x] = y 

n, q = map(int, input().split())
uf = UnionFind(n)
for i in range(q):
  com, x, y = map(int, input().split())
  if com == 0:
    uf.unite(x, y)
  elif com == 1:
    if uf.find(x) == uf.find(y):
      print(1)
    else:
      print(0)
