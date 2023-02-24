def dfs(u):
  global time
  time += 1
  check[u][0] = time
  for v in maps[u]:
    if check[v][0] == 0:
      dfs(v)
  time += 1
  check[u][1] = time

n = int(input())
maps = {}
check = [[0, 0] for _ in range(n+1)]
time = 0
for i in range(n):
  items = list(map(int, input().split()))
  u = items[0]
  k = items[1]
  maps[u] = items[2:]
for i in range(1, n+1):
  if check[i][0] == 0:
    dfs(i)
for i in range(1, n+1):
  print(i, check[i][0], check[i][1])