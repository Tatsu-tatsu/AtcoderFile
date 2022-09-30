# 以下自力回答
# 学び：1から順番に書いてみる。その上でdfs（深さ探索）で共通化する。ex.1,2と順番に書く。かぶり始めたら共通化。
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 再帰回数の上限を設定。

N, Q = map(int, input().split())
lines = [[] for i in range(N+1)]
for _ in range(N-1):
  a, b = map(int, input().split())
  lines[a].append(b) # 2辺の点の置き方はこれが良い
  lines[b].append(a)
counter = {}
for _ in range(Q):
  p, x = map(int, input().split())
  if p in counter:
    counter[p] += x
  else:
    counter[p] = x

def dfs(n, now):
  if now in counter:
    point[now] = point[n] + counter[now]
  else:
    point[now] = point[n]
  for line in lines[now]:
    if n != line:
      dfs(now, line)
  return

point = {}
if 1 in counter:
  point[1] = counter[1]
else:
  point[1] = 0
for line in lines[1]:
  dfs(1, line)

for i in range(1, N+1):
  print(point[i], end=" ")