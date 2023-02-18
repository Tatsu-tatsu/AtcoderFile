from collections import defaultdict
N, Q = map(int, input().split())
maps = defaultdict(set)
for i in range(Q):
  t, a, b = map(int, input().split())
  if t == 1:
    maps[a].add(b)
  elif t == 2:
    if b in maps[a]:
      maps[a].remove(b)
  elif t == 3:
    if b in maps[a] and a in maps[b]:
      print("Yes")
    else:
      print("No")
