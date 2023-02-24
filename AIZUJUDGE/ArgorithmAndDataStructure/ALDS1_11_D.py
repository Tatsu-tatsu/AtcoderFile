import sys
sys.setrecursionlimit(200000)
from collections import defaultdict
def dfs(i):
  global now
  groups[i] = now
  for j in maps[i]:
    if groups[j] == 0:
      dfs(j)

n, m = map(int, input().split())
maps = defaultdict(list)
groups = [0]*(n+1)
now = 0
for i in range(m):
  a, b = map(int, input().split())
  maps[a].append(b)
  maps[b].append(a)
for i in range(n):
  if groups[i] == 0:
    now += 1
    dfs(i)

q = int(input())
for i in range(q):
  s, t = map(int, input().split())
  if groups[s] == groups[t]:
    print('yes')
  else:
    print('no')
  