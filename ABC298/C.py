from collections import defaultdict
N = int(input())
Q = int(input())
items = [[] for _ in range(N)]
itemsMap = defaultdict(set)
for q in range(Q):
  t = list(map(int, input().split()))
  if t[0] == 1:
    i, j = t[1], t[2]
    items[j-1].append(i)
    itemsMap[i].add(j)
  elif t[0] == 2:
    i = t[1]
    items[i-1].sort()
    print(" ".join(map(str, items[i-1])))
  elif t[0] == 3:
    i = t[1]
    item = sorted(itemsMap[i])
    print(" ".join(map(str, item)))