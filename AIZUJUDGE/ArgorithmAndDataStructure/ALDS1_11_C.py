# 幅優先探索
# メモ：キューを使い、元々の値+1を入れていく。
from collections import deque
def bfs(u):
  for v in maps[u]:
    if check[v] == -1:
      que.append(v)
      check[v] = check[u] + 1

n = int(input())
maps = {}
que = deque()
check = [-1]*(n+1)
for i in range(n):
  items = list(map(int, input().split()))
  u = items[0]
  k = items[1]
  maps[u] = items[2:]
check[1] = 0
for v in maps[1]:
  que.append(v)
  check[v] = check[1] + 1
while que:
  bfs(que.popleft())
for i in range(1, n+1):
  print(i, check[i])