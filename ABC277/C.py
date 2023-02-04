# N = int(input())
# flagMap = {}
# flagMap[1] = True
# items = []
# for i in range(N):
#   a, b = map(int, input().split())
#   if a >= b:
#     items.append([b, a])
#   else:
#     items.append([a, b])
# sorted(items)
# for i in range(N):
#   if items[i][0] in flagMap.keys():
#     flagMap[items[i][1]] = True
#   if items[i][1] in flagMap.keys():
#     flagMap[items[i][0]] = True
# print(max(flagMap))

## 以下深さ優先探索
## ハマッた：原因は、再帰上限回数の上限を外すこと。
## Pythonでは再帰上限回数が設定されており、途中でエラーが発生する。それを外さないといけない。
import sys
sys.setrecursionlimit(200000)
def dfs(item):
  flagSet.add(item)
  if not item in itemsMap.keys():
    return
  for next in itemsMap[item]:
    if next in flagSet:
      continue
    dfs(next) 
  return

N = int(input())
itemsMap = {}
flagSet = set()
for i in range(N):
  a, b = map(int, input().split())
  if not a in itemsMap.keys():
    itemsMap[a] = []
  itemsMap[a].append(b)
  if not b in itemsMap.keys():
    itemsMap[b] = []
  itemsMap[b].append(a)
dfs(1)
print(max(flagSet))