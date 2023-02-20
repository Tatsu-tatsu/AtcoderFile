from collections import defaultdict
N, M = map(int, input().split())
maps = defaultdict(list)
for i in range(M):
  a, b = map(int, input().split())
  maps[a].append(b)
  maps[b].append(a)
for i in range(1,N+1):
  print(len(maps[i]), end=' ')
  maps[i].sort()
  print(' '.join(map(str, maps[i])))