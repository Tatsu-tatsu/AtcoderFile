# メモ
# 連結していない部分で閉路が出来るパターンを考慮する必要性があった。
import sys
sys.setrecursionlimit(10**7)

def dfs(item, before):
  past.add(item)
  for next in itemsMap[item]:
    if next == before:
      continue
    if next in past:
      ans[0] += 1
      continue
    dfs(next, item)
  return

N, M = map(int, input().split())
itemsMap = {}
past = set()
ans = [0]
for i in range(M):
  a, b = map(int, input().split())
  if not a in itemsMap.keys():
    itemsMap[a] = []
  itemsMap[a].append(b)
  if not b in itemsMap.keys():
    itemsMap[b] = []
  itemsMap[b].append(a)

dfs(1, 0)
print(int(ans[0]))

# 以下解説読んだ後
# ans = 辺の個数 - {(頂点の個数) - 連結成分の個数}
# 線の個数の最大値を求めたらいい。 
# 以下Dfs
# エラー点：線が一切ない頂点のとき、itemsMapに存在していないので連結成分にならない。
import sys
sys.setrecursionlimit(10**7)
def dfs(item):
  for next in itemsMap[item]:
    if next in past:
      continue
    past.add(next)
    dfs(next)
  return

N, M = map(int, input().split())
itemsMap = [[] for _ in range(N)]
past = set()
cnt = 0 # 連結成分の個数
for i in range(M):
  a, b = map(int, input().split())
  itemsMap[a-1].append(b-1)
  itemsMap[b-1].append(a-1)

for i in range(N):
  if i in past:
    continue
  past.add(i)
  dfs(i)
  cnt += 1
print(M - N + cnt)

# UnionFind木による解法
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
    self.parents[x] = y 


N, M = map(int, input().split())
uf = UnionFind(N)
ans = 0
for i in range(M):
  a, b = map(int, input().split())
  if uf.find(a-1) == uf.find(b-1):
    ans += 1
  uf.unite(a-1, b-1)

print(ans)
