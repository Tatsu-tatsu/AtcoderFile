# トポロジカルソートの問題
# トポロジカルソートを勉強したときに解き直す。
import sys
sys.setrecursionlimit(10**8)
def dfs(now):
  global num
  global clear
  if clear:
    return
  for next in left_to_right[now]:
    if clear:
      return
    if ans[next-1] == 0:
      num += 1
      ans[next-1] = num
      dfs(next)
  if not 0 in set(ans):
    clear = True
    return
  else:
    ans[now-1] = 0
    num -= 1

from collections import defaultdict
N, M = map(int, input().split())
left = set()
right = set()
left_to_right = defaultdict(list)
for i in range(M):
  x, y = map(int, input().split())
  left.add(x)
  right.add(y)
  left_to_right[x].append(y)
union = left | right
intersection = left & right
difference = left - right
if len(union) == N and len(intersection) == N-2 and len(difference) == 1:
  print('Yes')
else:
  print('No')
  exit()
min_item = difference.pop()
ans = [0]*N
ans[min_item-1] = 1
num = 1
now = min_item
clear = False
dfs(now)
print(' '.join(map(str, ans)))
