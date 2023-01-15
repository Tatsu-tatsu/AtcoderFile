# 一部エラー。理由不明
# メモ
# 1.深さ探索するときは、事前に空配列作成しておく。
# 2.1がindex0番だと非常にわかりにくいので、1同士を揃える。0は使わない。
def DFS(G, start):
  places[start] = True
  for u in G[start+1]:
    if places[u-1]:
      continue
    DFS(G, u-1)

N, M = map(int,input().split())
places = []
count = 0
G = {}
if M == 0:
  print(N)
  exit()
for j in range(N):
  places.append(False)
for i in range(M):
  u, v = map(int,input().split())
  if not u in G.keys():
    G[u] = []
  if not v in G.keys():
    G[v] = [] 
  G[u].append(v)
  G[v].append(u)

for i in range(N):
  if places[i]:
    continue
  DFS(G, i)
  count += 1
print(count)


# Answer
def dfs(v):
    seen[v] = True
    for next_v in e[v]:
        if not seen[next_v]:
            dfs(next_v)
 
n, m = map(int, input().split())
e = [[] for i in range(n + 1)]
seen = [False] * (n + 1)
for i in range(m):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
 
result = 0
for i in range(1, n + 1):
    if not seen[i]:
        result += 1
        dfs(i)
 
print(result)